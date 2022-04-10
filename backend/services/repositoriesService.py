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

    def get_public_repositories(self) -> list[dict[str, Any]]:
        return self.repository.get_all_public()

    def get_user_repositories(self, user_id: int) -> list[dict[str, Any]]:
        if self.users_service.is_valid_user(user_id):
            return self.repository.get_user_repositories(user_id)
        raise ItemNotFoundException(f"User with id {user_id} not found")

    def create_repository(self, repository_data: Optional[dict[str, Any]]) -> int:
        self.__validate_repository_data(repository_data)
        return self.repository.create_repository(repository_data)

    def __validate_repository_data(self, repository_data: Optional[dict[str, Any]]) -> None:
        if repository_data is None:
            raise MissingParameterException("Body is missing")
        if "owner" not in repository_data or "name" not in repository_data or "visibility" not in repository_data:
            raise MissingParameterException("One or more parameters are missing")
        if repository_data["name"] == '' or repository_data["visibility"] not in ["public", "private"]:
            raise InvalidParameterException("Invalid parameter")
        if not self.users_service.is_valid_user(repository_data["owner"]):
            raise ItemNotFoundException(f"User with id {repository_data['owner']} not found")

