from typing import Any

from exceptions.ItemNotFoundException import ItemNotFoundException
from repositories.taskRepository import TaskRepository
from services.repositoriesService import RepositoriesService
from services.usersService import UsersService


class TasksService:

    def __init__(self, task_repository: TaskRepository, users_service: UsersService,
                 repositories_service: RepositoriesService):
        self.repository = task_repository
        self.users_service = users_service
        self.repositories_service = repositories_service

    def get_user_tasks(self, user_id: int) -> list[dict[str, Any]]:
        if self.users_service.is_valid_user(user_id):
            return self.repository.get_user_tasks(user_id)
        raise ItemNotFoundException(f"User with id {user_id} not found")

    def get_repository_tasks(self, repository_id: int) -> list[dict[str, Any]]:
        if self.repositories_service.is_valid_repository(repository_id):
            return self.repository.get_repository_tasks(repository_id)
        raise ItemNotFoundException(f"Repository with id {repository_id} not found")
