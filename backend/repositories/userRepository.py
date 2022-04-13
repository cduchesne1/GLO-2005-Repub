from typing import Any, Optional

import bcrypt


class UserRepository:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

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
        self.cursor.execute("""UPDATE users SET 
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
