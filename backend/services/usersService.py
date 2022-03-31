from repositories import userRepository


def get_all_users():
    return userRepository.get_all_users()


def get_user(user_id):
    return userRepository.get_user(user_id)


def is_valid_user(user_id):
    user = get_user(user_id)
    return user is not None


def update_user(user_id, user_data):
    return userRepository.update_user(user_id, user_data)


def delete_user(user_id):
    return userRepository.delete_user(user_id)