from datetime import datetime
from typing import Any


class TaskRepository:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def __to_dto(self, row: tuple) -> dict[str, Any]:
        return {
            "id": row[0],
            "repository": row[1],
            "title": row[2],
            "assigned": row[3],
            "state": row[4],
            "creator": row[5],
            "timestamp": row[6],
            "number": row[7],
        }

    def __to_comment_dto(self, row: tuple) -> dict[str, Any]:
        return {
            "id": row[0],
            "task": row[1],
            "comment": row[2],
            "sender": row[3],
            "timestamp": row[4],
        }

    def get_all_tasks(self) -> list[dict[str, Any]]:
        self.cursor.execute("""
            SELECT * FROM tasks
        """)
        return [self.__to_dto(row) for row in self.cursor.fetchall()]

    def get_task(self, task_id: int) -> dict[str, Any]:
        self.cursor.execute("SELECT * FROM tasks WHERE id = %s", task_id)
        return self.__to_dto(self.cursor.fetchone())

    def get_user_tasks(self, user_id: int) -> list[dict[str, Any]]:
        self.cursor.execute("""
            SELECT * FROM tasks WHERE assigned = %s OR creator = %s
        """, (user_id, user_id))
        return [self.__to_dto(row) for row in self.cursor.fetchall()]

    def get_repository_tasks(self, repository_id: int) -> list[dict[str, Any]]:
        self.cursor.execute("""
            SELECT * FROM tasks WHERE repository = %s
        """, repository_id)
        return [self.__to_dto(row) for row in self.cursor.fetchall()]

    def create_task(self, task_data: dict[str, Any]) -> int:
        self.cursor.execute("SELECT MAX(num) FROM tasks WHERE repository = %s", task_data["repository"])
        result = self.cursor.fetchone()
        number = result[0] + 1 if result[0] is not None else 1
        self.cursor.execute(
            "INSERT INTO tasks (repository, title, description, assigned, state, creator, timestamp, num) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (task_data["repository"], task_data["title"],
             task_data["description"] if "description" in task_data else None, None,
             "open",
             task_data["creator"], datetime.now().strftime('%Y-%m-%d %H:%M:%S'), number))
        self.connection.commit()
        return self.cursor.lastrowid

    def update_task(self, task_id: int, task_data: dict[str, Any]) -> None:
        self.cursor.execute("""UPDATE tasks SET 
        title = IFNULL(%s, title), description = IFNULL(%s, description), 
        assigned = IFNULL(%s, assigned), state = IFNULL(%s, state)  WHERE id = %s;""",
                            (task_data["title"] if "title" in task_data else None,
                             task_data["description"] if "description" in task_data else None,
                             task_data["assigned"] if "assigned" in task_data else None,
                             task_data["state"] if "state" in task_data else None,
                             task_id))
        self.connection.commit()

    def delete_task(self, task_id: int) -> None:
        self.cursor.execute("DELETE FROM tasks WHERE id = %s", task_id)
        self.connection.commit()

    def get_task_repository(self, task_id: int) -> int:
        self.cursor.execute("SELECT repository FROM tasks WHERE id = %s", task_id)
        return self.cursor.fetchone()[0]

    def get_task_comments(self, task_id: int) -> list[dict[str, Any]]:
        self.cursor.execute("""
            SELECT * FROM comments WHERE task = %s
        """, task_id)
        return [self.__to_comment_dto(row) for row in self.cursor.fetchall()]

    def create_comment(self, task_id: int, comment_data: dict[str, Any]) -> int:
        self.cursor.execute("INSERT INTO comments (task, comment, sender, timestamp) VALUES (%s, %s, %s, %s)",
                            (task_id, comment_data["comment"], comment_data["sender"],
                             datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        self.connection.commit()
        return self.cursor.lastrowid
