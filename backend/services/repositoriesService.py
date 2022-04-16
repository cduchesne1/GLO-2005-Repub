from typing import Any, Optional

from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.ItemNotFoundException import ItemNotFoundException
from exceptions.MissingParameterException import MissingParameterException
from repositories.repositoryRepository import RepositoryRepository
from services.usersService import UsersService


class RepositoriesService:
    def __init__(self, repository: RepositoryRepository, users_service: UsersService):
        self.repository = repository
        self.users_service = users_service

    def get_repository(self, repository_id: int) -> dict[str, Any]:
        result = self.repository.get_repository(repository_id)
        if result is None:
            raise ItemNotFoundException(f"Repository with id {repository_id} not found")
        return result

    def get_public_repositories(self) -> list[dict[str, Any]]:
        return self.repository.get_all_public()

    def get_user_repositories(self, user_id: int) -> list[dict[str, Any]]:
        if self.users_service.is_valid_user(user_id):
            return self.repository.get_user_repositories(user_id)
        raise ItemNotFoundException(f"User with id {user_id} not found")

    def get_user_repository_by_username_and_name(self, username: str, repository_name: str) -> Optional[dict[str, Any]]:
        user = self.users_service.get_user_by_username(username)
        repository = self.repository.get_repository_by_user_id_and_name(user["id"], repository_name)
        if repository is None:
            raise ItemNotFoundException(f"Repository with name {repository_name} not found")
        return repository

    def create_repository(self, repository_data: Optional[dict[str, Any]]) -> int:
        self.__validate_repository_data(repository_data)
        return self.repository.create_repository(repository_data)

    def update_repository(self, repository_id: int, repository_data: Optional[dict[str, Any]]) -> None:
        if self.is_valid_repository(repository_id):
            self.__validate_repository_data_for_update(repository_data)
            return self.repository.update_repository(repository_id, repository_data)
        raise ItemNotFoundException(f"Repository with id {repository_id} not found")

    def delete_repository(self, repository_id: int) -> None:
        if self.is_valid_repository(repository_id):
            return self.repository.delete_repository(repository_id)
        raise ItemNotFoundException(f"Repository with id {repository_id} not found")

    def is_valid_repository(self, repository_id: int) -> bool:
        repository = self.get_repository(repository_id)
        return repository is not None

    def is_user_repository(self, repository_id: int, user_id: int) -> bool:
        repository = self.get_repository(repository_id)
        if repository is None or repository["owner"] != user_id:
            collaborators = self.repository.get_collaborators(repository_id)
            return user_id in collaborators
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

    def __validate_repository_data_for_update(self, repository_data: Optional[dict[str, Any]]) -> None:
        if "name" in repository_data and repository_data["name"] == '':
            raise InvalidParameterException("Invalid name")
        if "visibility" in repository_data and repository_data["visibility"] not in ["public", "private"]:
            raise InvalidParameterException("Invalid visibility")
