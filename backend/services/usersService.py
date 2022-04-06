import re

from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.MissingParameterException import MissingParameterException
from repositories import userRepository


def get_all_users():
    return userRepository.get_all_users()


def create_user(user_data):
    __validate_user_data(user_data)
    return userRepository.create_user(user_data)


def __validate_user_data(user_data):
    if 'email' not in user_data or 'username' not in user_data or 'name' not in user_data \
            or 'password' not in user_data:
        raise MissingParameterException('One or more parameters are missing')

    if user_data['email'] == '' or user_data['username'] == '' or user_data['name'] == '' \
            or user_data['password'] == '':
        raise InvalidParameterException('Invalid parameter')

    if not re.fullmatch(r'[^@]+@[^@]+\.[^@]+', user_data['email']):
        raise InvalidParameterException('Invalid email')
