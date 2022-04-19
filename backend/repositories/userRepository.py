import datetime
from typing import Any, Optional
from uuid import uuid4, UUID

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
            "name": row[0],
            "username": row[1],
            "email": row[2],
            "bio": row[3],
            "website": row[4],
            "company": row[5],
            "location": row[6],
        }

    def __to_public_dto(self, row: Any) -> dict[str, Any]:
        return {
            "name": row[0],
            "username": row[1],
            "bio": row[3],
            "website": row[4],
            "company": row[5],
            "location": row[6],
        }

    def get_all_users(self) -> list[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Users;")
            result = cursor.fetchall()
            return [self.__to_public_dto(row) for row in result]
        finally:
            connection.close()

    def get_filtered_users(self, filter) -> list[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            username_pattern = f"{filter}%"
            cursor.execute("SELECT * FROM Users WHERE username LIKE %s;", username_pattern)
            result = cursor.fetchall()
            return [self.__to_public_dto(row) for row in result]
        finally:
            connection.close()

    def create_user(self, user_data: dict[str, Any]) -> int:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Users (name, username, email, bio, website, company, location) VALUES (%s, %s, %s, NULL, NULL, NULL, NULL);",
                (user_data['name'], user_data['username'], user_data['email']))
            cursor.execute("INSERT INTO authentication (id, password) VALUES (%s, %s);",
                           (cursor.lastrowid, self.__encrypt_password(user_data['password'])))
            connection.commit()
            return cursor.lastrowid
        finally:
            connection.close()

    def __encrypt_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def get_user(self, username: str, public=True) -> Optional[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE username = %s;", username)
            result = cursor.fetchone()
            if result is None:
                return None
            if public:
                return self.__to_public_dto(result)
            return self.__to_dto(result)
        finally:
            connection.close()

    def get_user_by_email(self, email: str, public=True) -> Optional[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE email = %s;", email)
            result = cursor.fetchone()
            if result is None:
                return None
            if public:
                return self.__to_public_dto(result)
            return self.__to_dto(result)
        finally:
            connection.close()

    def update_user(self, username: str, user_data: dict[str, Any]) -> None:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("""UPDATE Users SET 
                    name = IFNULL(%s, name), username = IFNULL(%s, username), 
                    email = IFNULL(%s, email), bio = IFNULL(%s, bio), website = IFNULL(%s, website), 
                    company = IFNULL(%s, company), location = IFNULL(%s, location) WHERE username = %s;""",
                           (user_data["name"] if "name" in user_data else None,
                            user_data["username"] if "username" in user_data else None,
                            user_data["email"] if "email" in user_data else None,
                            user_data["bio"] if "bio" in user_data else None,
                            user_data["website"] if "website" in user_data else None,
                            user_data["company"] if "company" in user_data else None,
                            user_data["location"] if "location" in user_data else None, username))
            connection.commit()
        finally:
            connection.close()

    def delete_user(self, username: str, user_repositories: list[dict[str, Any]]) -> None:
        connection = self.__create_connection()
        try:
            for repo in user_repositories:
                self.git_repository.delete_repository(username, repo["name"])

            cursor = connection.cursor()
            cursor.execute("DELETE FROM Users WHERE username = %s;", username)
            connection.commit()
        finally:
            connection.close()

    def username_exists(self, username: str) -> bool:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE username = %s;", username)
            return cursor.fetchone() is not None
        finally:
            connection.close()

    def email_exists(self, email: str) -> bool:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE email = %s;", email)
            return cursor.fetchone() is not None
        finally:
            connection.close()

    def log_user(self, user_credential):
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            public_DTO = self.get_user_by_email(user_credential["email"])
            cursor.execute("SELECT password FROM Authentication WHERE email = %s", user_credential["email"])
            hashed_password_from_db = cursor.fetchone()[0]
            if hashed_password_from_db is None:
                raise InvalidParameterException("Password and email combination doesn't exist")

            passwd_to_check = bytes(hashed_password_from_db, 'utf-8')
            if bcrypt.checkpw(user_credential["password"].encode(), passwd_to_check):
                return {
                    "token_id": str(self.create_token(public_DTO["username"])),
                    "username": public_DTO["username"],
                    "name": public_DTO["name"]
                }
            else:
                raise InvalidParameterException("Password and email combination doesn't exist")
        finally:
            connection.close()

    def create_token(self, username: str):
        token_id = uuid4()
        token_creation_time = datetime.datetime.now()
        token_expire_time = datetime.datetime.now() + datetime.timedelta(days=1)
        new_token = {"token_id": token_id, "token_creation_time": token_creation_time,
                     "token_expire_time": token_expire_time, "username": username}
        self.tokens.append(new_token)
        return new_token["token_id"]

    def check_if_token_is_valid(self, token_id):
        print(token_id)
        print(self.tokens)
        token_is_valid = False
        for stocked_token in self.tokens:
            print(stocked_token["token_expire_time"], datetime.datetime.now())
            if stocked_token["token_expire_time"] < datetime.datetime.now():
                self.tokens.remove(stocked_token)
                continue
            if stocked_token["token_id"] == UUID(token_id):
                token_index = self.tokens.index(stocked_token)
                self.update_token(token_index)
                token_is_valid = True
        return token_is_valid

    def get_user_by_token(self, token_id):
        for stocked_token in self.tokens:
            if stocked_token["token_id"] == token_id:
                return stocked_token["username"]
        return None

    def update_token(self, token_index):
        self.tokens[token_index]["token_expire_time"] = datetime.datetime.now() + datetime.timedelta(days=1)

    def logout(self, token_id):
        for stocked_token in self.tokens:
            if stocked_token["token_id"] == token_id:
                self.tokens.remove(stocked_token)
                break
