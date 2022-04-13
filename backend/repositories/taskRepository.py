from typing import Any


class TaskRepository:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def __to_dto(self, row: tuple) -> dict[str, Any]:
        return {
            "id": row[0],
            "repository_id": row[1],
            "title": row[2],
            "assigned": row[3],
            "state": row[4],
            "creator": row[5],
            "timestamp": row[6],
            "number": row[7],
        }

    def get_user_tasks(self, user_id: int) -> list[dict[str, Any]]:
        self.cursor.execute("""
            SELECT * FROM tasks WHERE assigned = %s OR creator = %s
        """, (user_id, user_id))
        return [self.__to_dto(row) for row in self.cursor.fetchall()]
