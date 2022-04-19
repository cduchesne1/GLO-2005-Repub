import re
from typing import Any, Optional

from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.ItemNotFoundException import ItemNotFoundException
from exceptions.MissingParameterException import MissingParameterException
from repositories.repositoryRepository import RepositoryRepository
from repositories.userRepository import UserRepository


class UsersService:

    def __init__(self, user_repository: UserRepository, repository_repository: RepositoryRepository):
        self.repository = user_repository
        self.repository_repository = repository_repository

    def get_all_users(self) -> list[dict[str, Any]]:
        result = self.repository.get_all_users()
        if result is None:
            raise ItemNotFoundException("No users found")
        return result

    def get_filtered_users(self, filter) -> list[dict[str, Any]]:
        result = self.repository.get_filtered_users(filter)
        if result is None:
            raise ItemNotFoundException("No users found")
        return result

    def get_user(self, username: str, public=True) -> dict[str, Any]:
        result = self.repository.get_user(username, public=public)
        if result is None:
            raise ItemNotFoundException(f"User with username {username} not found")
        return result

    def update_user(self, username: str, user_data: Optional[dict[str, Any]]) -> None:
        if self.is_valid_user(username):
            self.__validate_user_data_for_update(user_data)
            return self.repository.update_user(username, user_data)
        raise ItemNotFoundException(f"User with username {username} not found")

    def delete_user(self, username: str) -> None:
        print("deleting")
        if self.is_valid_user(username):
            return self.repository.delete_user(username, self.repository_repository.get_user_repositories(username))
        raise ItemNotFoundException(f"User with username {username} not found")

    def create_user(self, user_data: Optional[dict[str, Any]]) -> int:
        self.__validate_user_data(user_data)
        return self.repository.create_user(user_data)

    def is_valid_user(self, username: str) -> bool:
        user = self.get_user(username)
        return user is not None

    def __validate_user_data(self, user_data: Optional[dict[str, Any]]) -> None:
        if 'email' not in user_data or 'username' not in user_data or 'name' not in user_data \
                or 'password' not in user_data:
            raise MissingParameterException('One or more parameters are missing')

        if user_data['email'] == '' or user_data['username'] == '' or user_data['name'] == '' \
                or user_data['password'] == '':
            raise InvalidParameterException('Invalid parameter')

        if not re.fullmatch(r'[^@]+@[^@]+\.[^@]+', user_data['email']):
            raise InvalidParameterException('Invalid email')

        if self.repository.username_exists(user_data['username']):
            raise InvalidParameterException('Username already exists')

        if self.repository.email_exists(user_data['email']):
            raise InvalidParameterException('Email already exists')

    def __validate_user_data_for_update(self, user_data: Optional[dict[str, Any]]) -> None:
        if "name" in user_data and user_data['name'] == '':
            raise InvalidParameterException('Invalid name')
        if "username" in user_data:
            if user_data['username'] == '':
                raise InvalidParameterException('Invalid username')
            if self.repository.username_exists(user_data['username']):
                raise InvalidParameterException('Username already exists')
        if "email" in user_data:
            if user_data['email'] == '':
                raise InvalidParameterException('Invalid email')
            if self.repository.email_exists(user_data['email']):
                raise InvalidParameterException('Email already exists')
