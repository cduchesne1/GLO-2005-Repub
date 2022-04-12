from typing import Any, Optional


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
            "collaborators": row[6].split(",") if row[6] else [],
            "tags": row[7].split(",") if row[7] else []
        }

    def get_repository(self, repository_id: int) -> Optional[dict[str, Any]]:
        self.cursor.execute(
        """SELECT r.id AS id, r.owner, r.name, r.visibility, r.description, r.website, 
            GROUP_CONCAT(DISTINCT c.user) AS collaborators, GROUP_CONCAT(DISTINCT t.tag) AS tags 
            FROM repositories r INNER JOIN tagged rt ON r.id = rt.repository INNER JOIN tags t on rt.tag = t.id
            LEFT OUTER JOIN collaborators c ON r.id = c.repository WHERE r.id = %s GROUP BY r.id;""",
            repository_id)
        result = self.cursor.fetchone()
        return self.__to_dto(result) if result else None

    def get_all_public(self) -> list[dict[str, Any]]:
        self.cursor.execute(
            """SELECT r.id AS id, r.owner, r.name, r.visibility, r.description, r.website, 
            GROUP_CONCAT(DISTINCT c.user) AS collaborators, GROUP_CONCAT(DISTINCT t.tag) AS tags 
            FROM repositories r INNER JOIN tagged rt ON r.id = rt.repository INNER JOIN tags t on rt.tag = t.id 
            LEFT OUTER JOIN collaborators c ON r.id = c.repository WHERE r.visibility = 'public' GROUP BY r.id;""")
        return [self.__to_dto(row) for row in self.cursor.fetchall()]

    def get_user_repositories(self, user_id: int) -> list[dict[str, Any]]:
        self.cursor.execute(
            """ SELECT r.id AS id, r.owner, r.name, r.visibility, r.description, r.website, 
            GROUP_CONCAT(DISTINCT c.user) AS collaborators, GROUP_CONCAT(DISTINCT t.tag) AS tags
            FROM repositories r INNER JOIN tagged rt ON r.id = rt.repository INNER JOIN tags t on rt.tag = t.id
            LEFT OUTER JOIN collaborators c ON r.id = c.repository WHERE r.owner = %s GROUP BY r.id;""", user_id)
        return [self.__to_dto(row) for row in self.cursor.fetchall()]

    def create_repository(self, repository_data: dict[str, Any]) -> int:
        self.cursor.execute(
            "INSERT INTO repositories (owner, name, visibility, description, website) VALUES (%s, %s, %s, %s, %s)",
            (repository_data["owner"], repository_data["name"], repository_data["visibility"],
             repository_data["description"] if "description" in repository_data else None,
             repository_data["website"] if "website" in repository_data else None))
        repo_id = self.cursor.lastrowid
        if "tags" in repository_data:
            self.cursor.executemany(
                "INSERT INTO tagged (repository, tag) VALUES (%s, %s)",
                [(repo_id, tag) for tag in self.convert_tags(repository_data["tags"])])
        self.connection.commit()
        return repo_id

    def update_repository(self, repository_id: int, repository_data: dict[str, Any]) -> None:
        self.cursor.execute(
            "UPDATE repositories SET name = %s, visibility = %s, description = %s, website = %s WHERE id = %s;",
            (repository_data["name"], repository_data["visibility"], repository_data["description"],
             repository_data["website"], repository_id))
        self.connection.commit()

    def delete_repository(self, repository_id: int) -> None:
        self.cursor.execute("DELETE FROM repositories WHERE id = %s;", repository_id)
        self.connection.commit()

    def convert_tags(self, tags: list[str]) -> list[int]:
        return [self.get_tag_id(tag) for tag in tags]

    def get_tag_id(self, tag: str) -> int:
        self.cursor.execute("SELECT id FROM tags WHERE tag = %s", tag)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            self.cursor.execute("INSERT INTO tags (tag) VALUES (%s)", tag)
            return self.cursor.lastrowid
