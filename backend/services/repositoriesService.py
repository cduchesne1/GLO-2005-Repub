from exceptions.ItemNotFoundException import ItemNotFoundException
from repositories.repositoryRepository import RepositoryRepository
from services.usersService import UsersService


class RepositoriesService:
    def __init__(self, repository: RepositoryRepository, users_service: UsersService):
        self.repository = repository
        self.users_service = users_service

    def get_user_repositories(self, user_id):
        if self.users_service.is_valid_user(user_id):
            return self.repository.get_user_repositories(user_id)
        raise ItemNotFoundException(f"User with id {user_id} not found")
