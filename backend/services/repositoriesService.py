from typing import Any, Optional

from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.ItemNotFoundException import ItemNotFoundException
from exceptions.MissingParameterException import MissingParameterException
from repositories.gitServerRepository import GitServerRepository
from repositories.repositoryRepository import RepositoryRepository
from services.usersService import UsersService


class RepositoriesService:
    def __init__(self, repository: RepositoryRepository, git_repository: GitServerRepository,
                 users_service: UsersService):
        self.repository = repository
        self.git_repository = git_repository
        self.users_service = users_service

    def get_repository(self, username: str, repository_name: str) -> dict[str, Any]:
        result = self.repository.get_repository(username, repository_name)
        if result is None:
            raise ItemNotFoundException(f"Repository with {username}/{repository_name} not found")
        return result

    def get_public_repositories(self) -> list[dict[str, Any]]:
        return self.repository.get_all_public()

    def get_repositories_by_filter(self, filter) -> list[dict[str, Any]]:
        return self.repository.get_filtered_repositories(filter)

    def get_user_repositories(self, username: str, public=False) -> list[dict[str, Any]]:
        if self.users_service.is_valid_user(username):
            return self.repository.get_user_repositories(
                username) if not public else self.repository.get_user_public_repositories(username)
        raise ItemNotFoundException(f"User with username {username} not found")

    def get_user_repository_files(self, username: str, repository_name: str, branch: str) -> list[str]:
        self.users_service.get_user(username)
        self.get_repository(username, repository_name)
        return self.git_repository.get_files(username, repository_name, branch)

    def get_repository_branches(self, username: str, repository_name: str) -> list[str]:
        self.users_service.get_user(username)
        self.get_repository(username, repository_name)
        return self.git_repository.get_branches(username, repository_name)

    def get_file_content(self, username: str, repository_name: str, branch: str, file_path: str) -> str:
        self.users_service.get_user(username)
        self.get_repository(username, repository_name)
        return self.git_repository.get_file_content(username, repository_name, branch, file_path)

    def create_repository(self, repository_data: Optional[dict[str, Any]]) -> str:
        self.__validate_repository_data(repository_data)
        return self.repository.create_repository(repository_data)

    def update_repository(self, username: str, repository_name: str, repository_data: Optional[dict[str, Any]]) -> None:
        if self.is_valid_repository(username, repository_name):
            self.__validate_repository_data_for_update(username, repository_name, repository_data)
            return self.repository.update_repository(username, repository_name, repository_data)
        raise ItemNotFoundException(f"Repository {username}/{repository_name} not found")

    def delete_repository(self, username: str, repository_name: str) -> None:
        if self.is_valid_repository(username, repository_name):
            return self.repository.delete_repository(username, repository_name)
        raise ItemNotFoundException(f"Repository {username}/{repository_name} not found")

    def is_valid_repository(self, username: str, repository_name: str) -> bool:
        repository = self.get_repository(username, repository_name)
        return repository is not None

    def is_user_repository(self, username: str, repository_name: str, creator: str) -> bool:
        if username != creator:
            collaborators = self.repository.get_collaborators(username, repository_name)
            return creator in collaborators
        return True

    def __validate_repository_data(self, repository_data: Optional[dict[str, Any]]) -> None:
        if repository_data is None:
            raise MissingParameterException("Body is missing")
        if "owner" not in repository_data or "name" not in repository_data or "visibility" not in repository_data:
            raise MissingParameterException("One or more parameters are missing")
        if repository_data["name"] == '' or repository_data["visibility"] not in ["public", "private"]:
            raise InvalidParameterException("Invalid parameter")
        if not self.users_service.is_valid_user(repository_data["owner"]):
            raise ItemNotFoundException(f"User with id {repository_data['owner']} not found")
        if self.repository.name_already_exists(repository_data["owner"], repository_data["name"]):
            raise InvalidParameterException(f"Repository with name {repository_data['name']} already exists")

    def __validate_repository_data_for_update(self, username: str, repository_name: str,
                                              repository_data: Optional[dict[str, Any]]) -> None:
        if "visibility" in repository_data and repository_data["visibility"] not in ["public", "private"]:
            raise InvalidParameterException("Invalid visibility")
        if "collaborators" in repository_data:
            repo = self.get_repository(username, repository_name)
            for collaborator in repository_data["collaborators"]:
                if repo["owner"] == collaborator:
                    raise InvalidParameterException("Owner can't be a collaborator")
