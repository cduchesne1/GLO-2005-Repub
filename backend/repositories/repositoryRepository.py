from typing import Any, Optional

import docker
import pymysql
from dotenv import load_dotenv

from repositories.gitServerRepository import GitServerRepository
from repositories.userRepository import UserRepository


class RepositoryRepository:
    def __init__(self, user_repository: UserRepository, git_repository: GitServerRepository):
        load_dotenv()
        self.client = docker.from_env()
        self.user_repository = user_repository
        self.git_repository = git_repository

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
            "owner": self.user_repository.get_user(row[0]),
            "name": row[1],
            "visibility": row[2],
            "description": row[3],
            "website": row[4],
            "collaborators": self.__collaborators_to_dto(row[5]),
            "tags": row[6].split(",") if row[6] else []
        }

    def __to_simple_dto(self, row: Any) -> dict[str, Any]:
        return {
            "owner": self.user_repository.get_user(row[0]),
            "name": row[1],
        }

    def __collaborators_to_dto(self, row: Any) -> list[dict[str, Any]]:
        collaborators = row.split(",") if row else []
        return list(
            map(lambda collaborator: self.user_repository.get_user(collaborator), collaborators))

    def get_repository(self, username: str, repository_name: str, simple=False) -> Optional[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT r.owner, r.name, r.visibility, r.description, r.website,
                GROUP_CONCAT(DISTINCT c.user) AS collaborators, GROUP_CONCAT(DISTINCT t.tag) AS tags
                FROM Repositories r LEFT OUTER JOIN Tagged rt ON r.owner = rt.owner AND r.name = rt.name LEFT OUTER JOIN Tags t on rt.tag = t.id
                LEFT OUTER JOIN Collaborators c ON r.owner = c.owner AND r.name = c.name WHERE r.owner = %s AND r.name = %s;""",
                (username, repository_name))
            result = cursor.fetchone()
            if result:
                return self.__to_dto(result) if not simple else self.__to_simple_dto(result)
            return None
        finally:
            connection.close()

    def get_all_public(self) -> list[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT r.owner, r.name, r.visibility, r.description, r.website,
                GROUP_CONCAT(DISTINCT c.user) AS collaborators, GROUP_CONCAT(DISTINCT t.tag) AS tags
                FROM Repositories r LEFT OUTER JOIN Tagged rt ON r.owner = rt.owner AND r.name = rt.name LEFT OUTER JOIN Tags t on rt.tag = t.id
                LEFT OUTER JOIN Collaborators c ON r.owner = c.owner WHERE r.visibility = 'public' GROUP BY r.owner, r.name;""")
            return [self.__to_dto(row) for row in cursor.fetchall()]
        finally:
            connection.close()

    def get_filtered_repositories(self, filter: str) -> list[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT r.owner, r.name, r.visibility, r.description, r.website,
                GROUP_CONCAT(DISTINCT c.user) AS collaborators, GROUP_CONCAT(DISTINCT t.tag) AS tags
                FROM Repositories r LEFT OUTER JOIN Tagged rt ON r.owner = rt.owner AND r.name = rt.name LEFT OUTER JOIN Tags t on rt.tag = t.id
                LEFT OUTER JOIN Collaborators c ON r.owner = c.owner WHERE r.name LIKE %s GROUP BY r.owner, r.name;""",
                (filter + "%",))
            return [self.__to_dto(row) for row in cursor.fetchall()]
        finally:
            connection.close()

    def get_user_repositories(self, username: str) -> list[dict[str, Any]]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT r.owner, r.name, r.visibility, r.description, r.website,
                GROUP_CONCAT(DISTINCT c.user) AS collaborators, GROUP_CONCAT(DISTINCT t.tag) AS tags
                FROM Repositories r LEFT OUTER JOIN Tagged rt ON r.owner = rt.owner AND r.name = rt.name LEFT OUTER JOIN Tags t on rt.tag = t.id
                LEFT OUTER JOIN Collaborators c ON r.owner = c.owner AND r.name = c.name WHERE r.owner = %s GROUP BY r.name;""",
                username)
            return [self.__to_dto(row) for row in cursor.fetchall()]
        finally:
            connection.close()

    def create_repository(self, repository_data: dict[str, Any]) -> str:
        self.git_repository.create_repository(repository_data["owner"], repository_data["name"])

        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Repositories (owner, name, visibility, description, website) VALUES (%s, %s, %s, %s, %s)",
                (repository_data["owner"], repository_data["name"], repository_data["visibility"],
                 repository_data["description"] if "description" in repository_data else None,
                 repository_data["website"] if "website" in repository_data else None))
            if "tags" in repository_data:
                cursor.executemany(
                    "INSERT INTO Tagged (owner, name, tag) VALUES (%s, %s, %s)",
                    [(repository_data["owner"], repository_data["name"], tag) for tag in
                     self.convert_tags(repository_data["tags"])])
            connection.commit()
            return f"{repository_data['owner']}/{repository_data['name']}"
        finally:
            connection.close()

    def update_repository(self, username: str, repository_name: str, repository_data: dict[str, Any]) -> None:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("""UPDATE Repositories SET 
                    visibility = IFNULL(%s, visibility), 
                    description = IFNULL(%s, description), website = IFNULL(%s, website) WHERE owner = %s AND name = %s;""",
                           (repository_data["visibility"] if "visibility" in repository_data else None,
                            repository_data["description"] if "description" in repository_data else None,
                            repository_data["website"] if "website" in repository_data else None,
                            username, repository_name))
            if "tags" in repository_data:
                cursor.execute("DELETE FROM Tagged WHERE owner = %s AND name = %s", (username, repository_name))
                cursor.executemany("INSERT INTO Tagged (owner, name, tag) VALUES (%s, %s, %s)",
                                   [(username, repository_name, tag) for tag in
                                    self.convert_tags(repository_data["tags"])])
            if "collaborators" in repository_data:
                cursor.execute("DELETE FROM Collaborators WHERE owner = %s AND name = %s", (username, repository_name))
                cursor.executemany("INSERT INTO Collaborators (user, owner, name) VALUES (%s, %s, %s)",
                                   [(user, username, repository_name) for user in repository_data["collaborators"]])
            connection.commit()
        finally:
            connection.close()

    def delete_repository(self, username: str, repository_name: str) -> None:
        connection = self.__create_connection()
        try:
            self.git_repository.delete_repository(username, repository_name)

            cursor = connection.cursor()
            cursor.execute("DELETE FROM Repositories WHERE owner = %s AND name = %s;", (username, repository_name))
            connection.commit()
        finally:
            connection.close()

    def get_collaborators(self, username: str, repository_name: str) -> list[str]:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """SELECT user FROM Collaborators WHERE owner = %s AND name = %s;""", (username, repository_name))
            return [row[0] for row in cursor.fetchall()]
        finally:
            connection.close()

    def convert_tags(self, tags: list[str]) -> list[int]:
        return [self.get_tag_id(tag) for tag in tags]

    def get_tag_id(self, tag: str) -> int:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM Tags WHERE tag = %s", tag)
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                cursor.execute("INSERT INTO Tags (tag) VALUES (%s)", tag)
                return cursor.lastrowid
        finally:
            connection.close()

    def name_already_exists(self, username: str, name: str) -> bool:
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Repositories WHERE name = %s AND owner = %s", (name, username))
            result = cursor.fetchone()
            return result is not None
        finally:
            connection.close()
