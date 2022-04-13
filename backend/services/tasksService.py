from typing import Any, Optional

from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.ItemNotFoundException import ItemNotFoundException
from exceptions.MissingParameterException import MissingParameterException
from repositories.taskRepository import TaskRepository
from services.repositoriesService import RepositoriesService
from services.usersService import UsersService


class TasksService:

    def __init__(self, task_repository: TaskRepository, users_service: UsersService,
                 repositories_service: RepositoriesService):
        self.repository = task_repository
        self.users_service = users_service
        self.repositories_service = repositories_service

    def get_all_tasks(self) -> list[dict[str, Any]]:
        result = self.repository.get_all_tasks()
        if result is None:
            raise ItemNotFoundException("No tasks found")
        return result

    def get_task(self, task_id: int) -> dict[str, Any]:
        result = self.repository.get_task(task_id)
        if result is None:
            raise ItemNotFoundException(f"Task with id {task_id} not found")
        return result

    def get_user_tasks(self, user_id: int) -> list[dict[str, Any]]:
        if self.users_service.is_valid_user(user_id):
            return self.repository.get_user_tasks(user_id)
        raise ItemNotFoundException(f"User with id {user_id} not found")

    def get_repository_tasks(self, repository_id: int) -> list[dict[str, Any]]:
        if self.repositories_service.is_valid_repository(repository_id):
            return self.repository.get_repository_tasks(repository_id)
        raise ItemNotFoundException(f"Repository with id {repository_id} not found")

    def create_task(self, task_data: dict[str, Any]) -> int:
        self.__validate_task_data(task_data)
        return self.repository.create_task(task_data)

    def update_task(self, task_id: int, task_data: dict[str, Any]) -> None:
        if self.is_valid_task(task_id):
            self.__validate_task_data_for_update(task_id, task_data)
            return self.repository.update_task(task_id, task_data)
        raise ItemNotFoundException(f"Task with id {task_id} not found")

    def delete_task(self, task_id: int) -> None:
        if self.is_valid_task(task_id):
            return self.repository.delete_task(task_id)
        raise ItemNotFoundException(f"Task with id {task_id} not found")

    def is_valid_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        return task is not None

    def __validate_task_data(self, task_data: Optional[dict[str, Any]]) -> None:
        if task_data is None:
            raise MissingParameterException("Body is missing")
        if "repository" not in task_data or "title" not in task_data or "creator" not in task_data:
            raise MissingParameterException("One or more parameters are missing")
        if task_data["title"] == '':
            raise InvalidParameterException("Invalid title")
        if not self.users_service.is_valid_user(task_data["creator"]):
            raise ItemNotFoundException(f"User with id {task_data['creator']} not found")
        if not self.repositories_service.is_user_repository(task_data["repository"], task_data["creator"]):
            raise ItemNotFoundException(f"Repository with id {task_data['repository']} not found")

    def __validate_task_data_for_update(self, task_id: int, task_data: Optional[dict[str, Any]]) -> None:
        if "title" in task_data and task_data["title"] == '':
            raise InvalidParameterException("Invalid title")
        if "assigned" in task_data:
            if not self.users_service.is_valid_user(task_data["assigned"]):
                raise ItemNotFoundException(f"User with id {task_data['assigned']} not found")
            repository = self.repository.get_task_repository(task_id)
            if not self.repositories_service.is_user_repository(repository, task_data["assigned"]):
                raise InvalidParameterException(f"Cannot assign task to user with id {task_data['assigned']}")
        if "state" in task_data:
            if task_data["state"] not in ["open", "closed"]:
                raise InvalidParameterException("Invalid state")