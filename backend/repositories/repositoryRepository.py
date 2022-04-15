from typing import Any, Optional

import pymysql

from repositories.userRepository import UserRepository


class RepositoryRepository:
    def __init__(self, user_repository: UserRepository):
        self.connection = pymysql.connect(host='localhost', user='user', password='password', db='mydb', port=42069)
        self.user_repository = user_repository
        self.cursor = self.connection.cursor()

    def __to_dto(self, row: Any) -> dict[str, Any]:
        return {
            "id": row[0],
            "owner": self.user_repository.get_user(row[1]),
            "name": row[2],
            "visibility": row[3],
            "description": row[4],
            "website": row[5],
            "collaborators": self.__collaborators_to_dto(row[6]),
            "tags": row[7].split(",") if row[7] else []
        }

    def __collaborators_to_dto(self, row: Any) -> list[dict[str, Any]]:
        collaborators = row.split(",") if row else []
        return list(
            map(lambda collaborator: self.user_repository.get_user(collaborator), collaborators))

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
        self.cursor.execute("""UPDATE repositories SET 
        name = IFNULL(%s, name), visibility = IFNULL(%s, visibility), 
        description = IFNULL(%s, description), website = IFNULL(%s, website) WHERE id = %s;""",
                            (repository_data["name"] if "name" in repository_data else None,
                             repository_data["visibility"] if "visibility" in repository_data else None,
                             repository_data["description"] if "description" in repository_data else None,
                             repository_data["website"] if "website" in repository_data else None, repository_id))
        self.connection.commit()

    def delete_repository(self, repository_id: int) -> None:
        self.cursor.execute("DELETE FROM repositories WHERE id = %s;", repository_id)
        self.connection.commit()

    def get_collaborators(self, repository_id: int) -> list[str]:
        self.cursor.execute(
            """SELECT user FROM collaborators WHERE repository = %s;""", repository_id)
        return [row[0] for row in self.cursor.fetchall()]

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
