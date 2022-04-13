import json

import pymysql
from flask import Flask, request, make_response
from flask_cors import CORS, cross_origin

from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.ItemNotFoundException import ItemNotFoundException
from exceptions.MissingParameterException import MissingParameterException
from repositories.repositoryRepository import RepositoryRepository
from repositories.taskRepository import TaskRepository
from repositories.userRepository import UserRepository
from services.repositoriesService import RepositoriesService
from services.tasksService import TasksService
from services.usersService import UsersService

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.register_error_handler(InvalidParameterException, lambda e: e)
app.register_error_handler(ItemNotFoundException, lambda e: e)
app.register_error_handler(MissingParameterException, lambda e: e)

cors = CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

connection = pymysql.connect(host='localhost', user='user', password='password', db='mydb')
user_repository = UserRepository(connection)
repository_repository = RepositoryRepository(connection)
task_repository = TaskRepository(connection)

users_service = UsersService(user_repository)
repositories_service = RepositoriesService(repository_repository, users_service)
tasks_service = TasksService(task_repository, users_service, repositories_service)


@app.route('/')
def heartbeat():
    return 'Welcome to RePub API', 200


@app.route('/login', methods=['POST'])
def login():
    return 'Login successful'


@app.route('/logout', methods=['POST'])
def logout():
    return 'Logout successful'


@app.route('/signup', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def signup():
    result = users_service.create_user(request.get_json())
    response = make_response()
    response.headers['Location'] = f'{request.url_root}users/{result}'
    return response, 201


@app.route('/users', methods=['GET'])
def users():
    result = users_service.get_all_users()
    return json.dumps({"users": list(result), "total": len(result)}), 200


@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def profile(user_id):
    if request.method == 'GET':
        result = users_service.get_user(user_id)
        return json.dumps(result), 200
    elif request.method == 'PUT':
        users_service.update_user(user_id, request.get_json())
        return 'User with id {} updated'.format(user_id), 200
    elif request.method == 'DELETE':
        users_service.delete_user(user_id)
        return 'User with id {} deleted'.format(user_id), 200
    else:
        return 'Method not allowed', 405


@app.route('/users/<int:user_id>/repositories', methods=['GET'])
def user_repositories(user_id):
    result = repositories_service.get_user_repositories(user_id)
    return json.dumps({"repositories": list(result), "total": len(result)}), 200


@app.route('/users/<int:user_id>/tasks', methods=['GET'])
def user_tasks(user_id):
    result = tasks_service.get_user_tasks(user_id)
    return json.dumps({"tasks": list(result), "total": len(result)}, default=str), 200


@app.route('/repositories', methods=['GET', 'POST'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def repositories():
    if request.method == 'GET':
        result = repositories_service.get_public_repositories()
        return json.dumps({"repositories": list(result), "total": len(result)}), 200
    elif request.method == 'POST':
        result = repositories_service.create_repository(request.get_json())
        response = make_response()
        response.headers['Location'] = f'{request.url_root}repositories/{result}'
        return response, 201
    else:
        return 'Method not allowed', 405


@app.route('/repositories/<int:repository_id>', methods=['GET', 'PUT', 'DELETE'])
def repository(repository_id):
    if request.method == 'GET':
        result = repositories_service.get_repository(repository_id)
        return json.dumps(result), 200
    elif request.method == 'PUT':
        repositories_service.update_repository(repository_id, request.get_json())
        return 'Repository with id {} updated'.format(repository_id), 200
    elif request.method == 'DELETE':
        repositories_service.delete_repository(repository_id)
        return 'Repository with id {} deleted'.format(repository_id), 200
    else:
        return 'Method not allowed', 405


@app.route('/repositories/<int:repository_id>/tasks', methods=['GET'])
def repository_issues(repository_id):
    result = tasks_service.get_repository_tasks(repository_id)
    return json.dumps({"tasks": list(result), "total": len(result)}, default=str), 200


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        result = tasks_service.get_all_tasks()
        return json.dumps({"tasks": list(result), "total": len(result)}, default=str), 200
    elif request.method == 'POST':
        result = tasks_service.create_task(request.get_json())
        response = make_response()
        response.headers['Location'] = f'{request.url_root}tasks/{result}'
        return response, 201
    else:
        return 'Method not allowed', 405


@app.route('/tasks/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
def task(task_id):
    if request.method == 'GET':
        result = tasks_service.get_task(task_id)
        return json.dumps(result), 200
    elif request.method == 'PUT':
        tasks_service.update_task(task_id, request.get_json())
        return 'Task with id {} updated'.format(task_id), 200
    elif request.method == 'DELETE':
        tasks_service.delete_task(task_id)
        return 'Task with id {} deleted'.format(task_id), 200


@app.route('/tasks/<int:task_id>/comments', methods=['GET', 'POST'])
def task_comments(task_id):
    return 'Task {} comments'.format(task_id)


@app.route('/tasks/<int:task_id>/comments/<int:comment_id>', methods=['GET', 'PUT', 'DELETE'])
def task_comment(task_id, comment_id):
    return 'Task {} comment {}'.format(task_id, comment_id)
