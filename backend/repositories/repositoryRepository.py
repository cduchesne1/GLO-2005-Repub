from typing import Any

from pymysql import NULL


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

    def get_all_public(self) -> list[dict[str, Any]]:
        self.cursor.execute(
            "SELECT * FROM repositories WHERE visibility = 'public'")
        return [self.__to_dto(row) for row in self.cursor.fetchall()]

    def get_user_repositories(self, user_id: int) -> list[dict[str, Any]]:
        self.cursor.execute(
            "SELECT * FROM repositories WHERE owner = %s", user_id)
        return [self.__to_dto(row) for row in self.cursor.fetchall()]

    def create_repository(self, repository_data: dict[str, Any]) -> int:
        self.cursor.execute(
            "INSERT INTO repositories (owner, name, visibility, description, website) VALUES (%s, %s, %s, %s, %s)",
            (repository_data["owner"], repository_data["name"], repository_data["visibility"],
             repository_data["description"] if "description" in repository_data else None,
             repository_data["website"] if "website" in repository_data else None))
        self.connection.commit()
        return self.cursor.lastrowid
