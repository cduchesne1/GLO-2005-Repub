from datetime import datetime
from typing import Any, Tuple

import pymysql

from repositories.repositoryRepository import RepositoryRepository
from repositories.userRepository import UserRepository


class TaskRepository:
    def __init__(self, user_repository: UserRepository, repository_repository: RepositoryRepository):
        self.user_repository = user_repository
        self.repository_repository = repository_repository

    def __create_connection(self) -> pymysql.Connection:
        return pymysql.connect(
            host='localhost',
            user='user',
            password='password',
            db='mydb',
            port=42069
        )

    def __to_dto(self, row: tuple) -> dict[str, Any]:
        return {
            "id": row[0],
            "repository": self.repository_repository.get_repository(row[1], row[2], simple=True),
            "title": row[3],
            "description": row[4],
            "assigned": self.user_repository.get_user(row[5]) if row[5] is not None else None,
            "state": row[6],
            "creator": self.user_repository.get_user(row[7]),
            "timestamp": row[8],
            "number": row[9],
        }

    def __to_comment_dto(self, row: tuple) -> dict[str, Any]:
        return {
            "id": row[0],
            "task": row[1],
            "comment": row[2],
            "sender": self.user_repository.get_user(row[3]),
            "timestamp": row[4],
        }

    def get_all_tasks(self) -> list[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("""
                        SELECT * FROM Tasks
                    """)
            return [self.__to_dto(row) for row in cursor.fetchall()]
        finally:
            connection.close()

    def get_task(self, task_id: int) -> dict[str, Any]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Tasks WHERE id = %s", task_id)
            return self.__to_dto(cursor.fetchone())
        finally:
            connection.close()

    def get_task_by_repository_and_number(self, username: str, repository_name: str, number: int) -> dict[str, Any]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("""
                        SELECT * FROM Tasks WHERE owner = %s AND name= %s AND num = %s
                    """, (username, repository_name, number))
            return self.__to_dto(cursor.fetchone())
        finally:
            connection.close()

    def get_user_tasks(self, username: str) -> list[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("""
                        SELECT * FROM Tasks WHERE assigned = %s OR creator = %s
                    """, (username, username))
            return [self.__to_dto(row) for row in cursor.fetchall()]
        finally:
            connection.close()

    def get_repository_tasks(self, username: str, repository_name: str) -> list[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("""
                        SELECT * FROM Tasks WHERE owner = %s AND name= %s
                    """, (username, repository_name))
            return [self.__to_dto(row) for row in cursor.fetchall()]
        finally:
            connection.close()

    def create_task(self, task_data: dict[str, Any]) -> int:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT MAX(num) FROM Tasks WHERE owner = %s AND name = %s",
                           (task_data["owner"], task_data["name"]))
            result = cursor.fetchone()
            number = result[0] + 1 if result[0] is not None else 1
            cursor.execute(
                """INSERT INTO Tasks (owner, name, title, description, assigned, state, creator, timestamp, num) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (task_data["owner"], task_data["name"], task_data["title"],
                 task_data["description"] if "description" in task_data else None, None,
                 "open",
                 task_data["creator"], datetime.now().strftime('%Y-%m-%d %H:%M:%S'), number))
            connection.commit()
            return cursor.lastrowid
        finally:
            connection.close()

    def update_task(self, task_id: int, task_data: dict[str, Any]) -> None:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("""UPDATE Tasks SET 
                    title = IFNULL(%s, title), description = IFNULL(%s, description), 
                    assigned = IFNULL(%s, assigned), state = IFNULL(%s, state)  WHERE id = %s;""",
                           (task_data["title"] if "title" in task_data else None,
                            task_data["description"] if "description" in task_data else None,
                            task_data["assigned"] if "assigned" in task_data else None,
                            task_data["state"] if "state" in task_data else None,
                            task_id))
            connection.commit()
        finally:
            connection.close()

    def delete_task(self, task_id: int) -> None:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Tasks WHERE id = %s", task_id)
            connection.commit()
        finally:
            connection.close()

    def get_task_repository(self, task_id: int) -> Tuple[str, str]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT owner, name FROM Tasks WHERE id = %s", task_id)
            result = cursor.fetchone()
            return result[0], result[1]
        finally:
            connection.close()

    def get_task_comments(self, task_id: int) -> list[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("""
                        SELECT * FROM Comments WHERE task = %s
                    """, task_id)
            return [self.__to_comment_dto(row) for row in cursor.fetchall()]
        finally:
            connection.close()

    def get_comment(self, comment_id: int) -> dict[str, Any]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Comments WHERE id = %s", comment_id)
            return self.__to_comment_dto(cursor.fetchone())
        finally:
            connection.close()

    def create_comment(self, task_id: int, comment_data: dict[str, Any]) -> int:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Comments (task, comment, sender, timestamp) VALUES (%s, %s, %s, %s)",
                           (task_id, comment_data["comment"], comment_data["sender"],
                            datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            connection.commit()
            return cursor.lastrowid
        finally:
            connection.close()

    def update_comment(self, comment_id: int, comment_data: dict[str, Any]) -> None:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE Comments SET comment = IFNULL(%s, comment)  WHERE id = %s;",
                           (comment_data["comment"] if "comment" in comment_data else None,
                            comment_id))
            connection.commit()
        finally:
            connection.close()

    def delete_comment(self, comment_id: int) -> None:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Comments WHERE id = %s", comment_id)
            connection.commit()
        finally:
            connection.close()
