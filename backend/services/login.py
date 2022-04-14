import re

from repositories import userRepository
from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.MissingParameterException import MissingParameterException

class Logger:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def log_user(self, user_credential):
        self.__verify_credential(user_credential)
        return self.user_repository.log_user(user_credential)

    def __verify_credential(self, user_credential):
        if "email" not in user_credential or "password" not in user_credential:
            raise MissingParameterException('email or password is missing for login')

        if user_credential['email'] == '' or user_credential['password'] == '':
            raise InvalidParameterException('Invalid parameter')

        if not re.fullmatch(r'[^@]+@[^@]+\.[^@]+', user_credential['email']):
            raise InvalidParameterException('Invalid email')

    def check_if_token_is_valid(self, token_id):
        if token_id == "":
            raise InvalidParameterException("token_id is empty")
        return self.user_repository.check_if_token_is_valid(token_id)
