from typing import Any, Optional

import pymysql

from repositories.userRepository import UserRepository


class RepositoryRepository:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

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
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT r.id AS id, r.owner, r.name, r.visibility, r.description, r.website, 
                    GROUP_CONCAT(DISTINCT c.user) AS collaborators, GROUP_CONCAT(DISTINCT t.tag) AS tags 
                    FROM repositories r INNER JOIN tagged rt ON r.id = rt.repository INNER JOIN tags t on rt.tag = t.id
                    LEFT OUTER JOIN collaborators c ON r.id = c.repository WHERE r.id = %s GROUP BY r.id;""",
                repository_id)
            result = cursor.fetchone()
            return self.__to_dto(result) if result else None
        finally:
            connection.close()

    def get_all_public(self) -> list[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT r.id AS id, r.owner, r.name, r.visibility, r.description, r.website, 
                GROUP_CONCAT(DISTINCT c.user) AS collaborators, GROUP_CONCAT(DISTINCT t.tag) AS tags 
                FROM repositories r INNER JOIN tagged rt ON r.id = rt.repository INNER JOIN tags t on rt.tag = t.id 
                LEFT OUTER JOIN collaborators c ON r.id = c.repository WHERE r.visibility = 'public' GROUP BY r.id;""")
            return [self.__to_dto(row) for row in cursor.fetchall()]
        finally:
            connection.close()

    def get_user_repositories(self, user_id: int) -> list[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """ SELECT r.id AS id, r.owner, r.name, r.visibility, r.description, r.website, 
                GROUP_CONCAT(DISTINCT c.user) AS collaborators, GROUP_CONCAT(DISTINCT t.tag) AS tags
                FROM repositories r INNER JOIN tagged rt ON r.id = rt.repository INNER JOIN tags t on rt.tag = t.id
                LEFT OUTER JOIN collaborators c ON r.id = c.repository WHERE r.owner = %s GROUP BY r.id;""", user_id)
            return [self.__to_dto(row) for row in cursor.fetchall()]
        finally:
            connection.close()

    def get_repository_by_user_id_and_name(self, user_id: int, name: str) -> Optional[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT r.id AS id, r.owner, r.name, r.visibility, r.description, r.website, 
                GROUP_CONCAT(DISTINCT c.user) AS collaborators, GROUP_CONCAT(DISTINCT t.tag) AS tags 
                FROM repositories r INNER JOIN tagged rt ON r.id = rt.repository INNER JOIN tags t on rt.tag = t.id 
                LEFT OUTER JOIN collaborators c ON r.id = c.repository WHERE r.owner = %s AND r.name = %s GROUP BY r.id;""",
                (user_id, name))
            result = cursor.fetchone()
            return self.__to_dto(result) if result else None
        finally:
            connection.close()

    def create_repository(self, repository_data: dict[str, Any]) -> int:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO repositories (owner, name, visibility, description, website) VALUES (%s, %s, %s, %s, %s)",
                (repository_data["owner"], repository_data["name"], repository_data["visibility"],
                 repository_data["description"] if "description" in repository_data else None,
                 repository_data["website"] if "website" in repository_data else None))
            repo_id = cursor.lastrowid
            if "tags" in repository_data:
                cursor.executemany(
                    "INSERT INTO tagged (repository, tag) VALUES (%s, %s)",
                    [(repo_id, tag) for tag in self.convert_tags(repository_data["tags"])])
            connection.commit()
            return repo_id
        finally:
            connection.close()

    def update_repository(self, repository_id: int, repository_data: dict[str, Any]) -> None:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("""UPDATE repositories SET 
                    name = IFNULL(%s, name), visibility = IFNULL(%s, visibility), 
                    description = IFNULL(%s, description), website = IFNULL(%s, website) WHERE id = %s;""",
                           (repository_data["name"] if "name" in repository_data else None,
                            repository_data["visibility"] if "visibility" in repository_data else None,
                            repository_data["description"] if "description" in repository_data else None,
                            repository_data["website"] if "website" in repository_data else None, repository_id))
            connection.commit()
        finally:
            connection.close()

    def delete_repository(self, repository_id: int) -> None:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM repositories WHERE id = %s;", repository_id)
            connection.commit()
        finally:
            connection.close()

    def get_collaborators(self, repository_id: int) -> list[str]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT user FROM collaborators WHERE repository = %s;""", repository_id)
            return [row[0] for row in cursor.fetchall()]
        finally:
            connection.close()

    def convert_tags(self, tags: list[str]) -> list[int]:
        return [self.get_tag_id(tag) for tag in tags]

    def get_tag_id(self, tag: str) -> int:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM tags WHERE tag = %s", tag)
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                cursor.execute("INSERT INTO tags (tag) VALUES (%s)", tag)
                return cursor.lastrowid
        finally:
            connection.close()
