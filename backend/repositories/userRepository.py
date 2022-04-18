import datetime
from typing import Any, Optional
from uuid import uuid4

import bcrypt
import pymysql

from exceptions.InvalidParameterException import InvalidParameterException
from repositories.gitServerRepository import GitServerRepository


class UserRepository:
    def __init__(self, git_repository: GitServerRepository):
        self.git_repository = git_repository
        self.tokens = []

    def __create_connection(self) -> pymysql.Connection:
        return pymysql.connect(
            host='localhost',
            user='user',
            password='password',
            db='mydb',
            port=42069
        )

    def __to_dto(self, row: Any) -> dict[str, Any]:
        return {
            "id": row[0],
            "name": row[1],
            "username": row[2],
            "email": row[3],
            "bio": row[4],
            "website": row[5],
            "company": row[6],
            "location": row[7],
        }

    def __to_public_dto(self, row: Any) -> dict[str, Any]:
        return {
            "id": row[0],
            "name": row[1],
            "username": row[2],
            "bio": row[4],
            "website": row[5],
            "company": row[6],
            "location": row[7],
        }

    def get_all_users(self) -> list[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users;")
            result = cursor.fetchall()
            return [self.__to_public_dto(row) for row in result]
        finally:
            connection.close()

    def create_user(self, user_data: dict[str, Any]) -> int:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO users (name, username, email, bio, website, company, location) VALUES (%s, %s, %s, NULL, NULL, NULL, NULL);",
                (user_data['name'], user_data['username'], user_data['email']))
            cursor.execute("INSERT INTO authentication (id, password) VALUES (%s, %s);",
                           (cursor.lastrowid, self.__encrypt_password(user_data['password'])))
            connection.commit()
            return cursor.lastrowid
        finally:
            connection.close()

    def __encrypt_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def get_user(self, user_id: int, public=True) -> Optional[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
            result = cursor.fetchone()
            if result is None:
                return None
            if public:
                return self.__to_public_dto(result)
            return self.__to_dto(result)
        finally:
            connection.close()

    def get_user_by_username(self, username: str, public=True) -> Optional[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s;", username)
            result = cursor.fetchone()
            if result is None:
                return None
            if public:
                return self.__to_public_dto(result)
            return self.__to_dto(result)
        finally:
            connection.close()

    def update_user(self, user_id: int, user_data: dict[str, Any]) -> None:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("""UPDATE users SET 
                    name = IFNULL(%s, name), username = IFNULL(%s, username), 
                    email = IFNULL(%s, email), bio = IFNULL(%s, bio), website = IFNULL(%s, website), 
                    company = IFNULL(%s, company), location = IFNULL(%s, location) WHERE id = %s;""",
                           (user_data["name"] if "name" in user_data else None,
                            user_data["username"] if "username" in user_data else None,
                            user_data["email"] if "email" in user_data else None,
                            user_data["bio"] if "bio" in user_data else None,
                            user_data["website"] if "website" in user_data else None,
                            user_data["company"] if "company" in user_data else None,
                            user_data["location"] if "location" in user_data else None, user_id))
            connection.commit()
        finally:
            connection.close()

    def delete_user(self, user_id: int, user_repositories: list[dict[str, Any]]) -> None:
        connection = self.__create_connection()
        try:
            for repo in user_repositories:
                self.git_repository.delete_repository(repo["owner"]["username"], repo["name"])

            cursor = connection.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
            connection.commit()
        finally:
            connection.close()

    def username_exists(self, username: str) -> bool:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s;", username)
            return cursor.fetchone() is not None
        finally:
            connection.close()

    def email_exists(self, email: str) -> bool:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE email = %s;", email)
            return cursor.fetchone() is not None
        finally:
            connection.close()

    def log_user(self, user_credential):
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            user_id = self.__get_user_id(user_credential["email"])
            hashed_password_from_credential = bcrypt.hashpw(user_credential["password"], bcrypt.gensalt())
            cursor.execute("SELECT password FROM authentication WHERE id = %s", user_id)
            hashed_password_from_db = cursor.fetchone()
            if hashed_password_from_db is None:
                raise InvalidParameterException("Password and email combination doesn't exist")

            if bcrypt.checkpw(hashed_password_from_credential, hashed_password_from_db):
                return self.create_token()
            else:
                raise InvalidParameterException("Password and email combination doesn't exist")
        finally:
            connection.close()

    def create_token(self):
        token_id = uuid4()
        token_creation_time = datetime.datetime.now()
        token_expire_time = datetime.datetime.now() + datetime.timedelta(days=1)
        new_token = {"token_id": token_id, "token_creation_time": token_creation_time,
                     "token_expire_time": token_expire_time}
        self.tokens.append(new_token)
        return new_token["token_id"]

    def __get_user_id(self, email):
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM users WHERE email = %s", email)
            user_id = cursor.fetchone()
            if user_id is None:
                raise InvalidParameterException("email doesn't exist")
            return user_id
        finally:
            connection.close()

    def check_if_token_is_valid(self, token_id):
        token_is_valid = False
        for stocked_token in self.tokens:
            if stocked_token["token_expire_time"] < datetime.datetime.now():
                self.tokens.remove(stocked_token)
                continue
            if stocked_token["token_id"] == token_id:
                token_index = self.tokens.index(stocked_token)
                self.update_token(token_index)
                token_is_valid = True
        return token_is_valid

    def update_token(self, token_index):
        self.tokens[token_index]["token_expire_time"] = datetime.datetime.now()

    def logout(self, token_id):
        for stocked_token in self.tokens:
            if stocked_token["token_id"] == token_id:
                self.tokens.remove(stocked_token)
                break
