from pickle import FALSE
from typing import Any, Optional
import bcrypt
from uuid import uuid4
import datetime
from exceptions import InvalidParameterException
from exceptions import TokenExpiredException

class UserRepository:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.tokens = []

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

    def get_all_users(self) -> list[dict[str, Any]]:
        self.cursor.execute("SELECT * FROM users;")
        result = self.cursor.fetchall()
        return [self.__to_dto(row) for row in result]

    def create_user(self, user_data: dict[str, Any]) -> int:
        self.cursor.execute(
            "INSERT INTO users (name, username, email, bio, website, company, location) VALUES (%s, %s, %s, NULL, NULL, NULL, NULL);",
            (user_data['name'], user_data['username'], user_data['email']))
        self.cursor.execute("INSERT INTO authentication (id, password) VALUES (%s, %s);",
                            (self.cursor.lastrowid, self.__encrypt_password(user_data['password'])))
        self.connection.commit()
        return self.cursor.lastrowid

    def __encrypt_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def get_user(self, user_id: int) -> Optional[dict[str, Any]]:
        self.cursor.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
        result = self.cursor.fetchone()
        return self.__to_dto(result) if result else None

    def update_user(self, user_id: int, user_data: dict[str, Any]) -> None:
        self.cursor.execute(
            "UPDATE users SET name = %s, username = %s, email = %s, bio = %s, website = %s, company = %s, location = %s WHERE id = %s;",
            (user_data["name"], user_data["username"], user_data["email"], user_data["bio"], user_data["website"],
             user_data["company"], user_data["location"], user_id))
        self.connection.commit()

    def delete_user(self, user_id: int) -> None:
        self.cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
        self.connection.commit()

    def username_exists(self, username: str) -> bool:
        self.cursor.execute("SELECT * FROM users WHERE username = %s;", username)
        return self.cursor.fetchone() is not None

    def email_exists(self, email: str) -> bool:
        self.cursor.execute("SELECT * FROM users WHERE email = %s;", email)
        return self.cursor.fetchone() is not None

    def log_user(self, user_credential):
        user_id = self.__get_user_id(user_credential["email"])
        hashed_password_from_credential = bcrypt.hashpw(user_credential["password"], bcrypt.gensalt())
        self.cursor.execute("SELECT password FROM authentication WHERE id = %s", user_id)
        hashed_password_from_db = self.cursor.fetchone()
        if hashed_password_from_db is None:
            raise InvalidParameterException("Password and email combination doesn't exist")
        
        if bcrypt.checkpw(hashed_password_from_credential, hashed_password_from_db):
            return self.create_token()
        else:
            raise InvalidParameterException("Password and email combination doesn't exist")

    def create_token(self):
        token_id = uuid4()
        token_creation_time = datetime.datetime.now()
        token_expire_time = datetime.datetime.now() + datetime.timedelta(days=1)
        new_token = {"token_id": token_id, "token_creation_time": token_creation_time, "token_expire_time": token_expire_time }
        self.tokens.append(new_token)
        return new_token

    def __get_user_id(self, email):
        self.cursor.execute("SELECT id FROM users WHERE email = %s", email)
        user_id = self.cursor.fetchone()
        if user_id is None:
            raise InvalidParameterException("email doesn't exist")
        return user_id

    def check_if_token_is_valid(self, token):
        for stocked_token in self.tokens:
            if stocked_token["token_expire_time"] < datetime.datetime.now():
                self.tokens.remove(stocked_token)
                continue
            if stocked_token["token_id"] == token["token_id"]:
                self.update_token(token)
                return True
        return False

    def update_token(self, token):
        pass