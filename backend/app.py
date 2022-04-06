import json

from flask import Flask, request, make_response

from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.ItemNotFoundException import ItemNotFoundException
from exceptions.MissingParameterException import MissingParameterException
from services.usersService import get_all_users, create_user

app = Flask(__name__)
app.register_error_handler(InvalidParameterException, lambda e: e)
app.register_error_handler(ItemNotFoundException, lambda e: e)
app.register_error_handler(MissingParameterException, lambda e: e)


@app.route('/')
def heartbeat():
    return 'Welcome to RePub API'


@app.route('/login', methods=['POST'])
def login():
    return 'Login successful'


@app.route('/logout', methods=['POST'])
def logout():
    return 'Logout successful'


@app.route('/signup', methods=['POST'])
def signup():
    result = create_user(request.get_json())
    response = make_response()
    response.headers['Location'] = '/users/{}'.format(result)
    return response, 201


@app.route('/users', methods=['GET'])
def users():
    result = get_all_users()
    if result is None:
        return 'No users found', 404
    return json.dumps({"users": list(result), "total": len(result)}), 200


@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def profile(user_id):
    return 'User {}'.format(user_id)


@app.route('/users/<int:user_id>/repositories', methods=['GET'])
def user_repositories(user_id):
    return 'User {} repositories'.format(user_id)


@app.route('/users/<int:user_id>/tasks', methods=['GET'])
def user_tasks(user_id):
    return 'User {} tasks'.format(user_id)


@app.route('/repositories', methods=['GET', 'POST'])
def repositories():
    return 'Repositories list'


@app.route('/repositories/<int:repository_id>', methods=['GET', 'PUT', 'DELETE'])
def repository(repository_id):
    return 'Repository {}'.format(repository_id)


@app.route('/repositories/<int:repository_id>/tasks', methods=['GET'])
def repository_issues(repository_id):
    return 'Repository {} issues'.format(repository_id)


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    return 'Tasks list'


@app.route('/tasks/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
def task(task_id):
    return 'Task {}'.format(task_id)


@app.route('/tasks/<int:task_id>/comments', methods=['GET', 'POST'])
def task_comments(task_id):
    return 'Task {} comments'.format(task_id)


@app.route('/tasks/<int:task_id>/comments/<int:comment_id>', methods=['GET', 'PUT', 'DELETE'])
def task_comment(task_id, comment_id):
    return 'Task {} comment {}'.format(task_id, comment_id)
