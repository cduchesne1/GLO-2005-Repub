from typing import Any


class RepositoryRepository:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def __to_dto(self, row: Any) -> dict[str, Any]:
        return {
            "id": row[0],
            "owner": row[1],
            "name": row[2],
            "visibility": row[3],
            "description": row[4],
            "website": row[5],
        }

    def get_user_repositories(self, user_id: int) -> list[dict[str, Any]]:
        self.cursor.execute(
            "SELECT * FROM repositories WHERE owner = %s", user_id)
        return [self.__to_dto(row) for row in self.cursor.fetchall()]
