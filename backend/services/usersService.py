import re

from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.ItemNotFoundException import ItemNotFoundException
from exceptions.MissingParameterException import MissingParameterException
from repositories import userRepository


def get_all_users():
    result = userRepository.get_all_users()
    if result is None:
        raise ItemNotFoundException("No users found")
    return result


def get_user(user_id):
    result = userRepository.get_user(user_id)
    if result is None:
        raise ItemNotFoundException(f"User with id {user_id} not found")
    return result


def is_valid_user(user_id):
    user = get_user(user_id)
    return user is not None


def update_user(user_id, user_data):
    if is_valid_user(user_id):
        userRepository.update_user(user_id, user_data)
    else:
        raise ItemNotFoundException(f"User with id {user_id} not found")


def delete_user(user_id):
    if is_valid_user(user_id):
        userRepository.delete_user(user_id)
    else:
        raise ItemNotFoundException(f"User with id {user_id} not found")


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