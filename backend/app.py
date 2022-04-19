import json
import os

from flask import Flask, request, send_file
from flask_cors import CORS

from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.ItemNotFoundException import ItemNotFoundException
from exceptions.MissingParameterException import MissingParameterException
from repositories.gitServerRepository import GitServerRepository
from repositories.repositoryRepository import RepositoryRepository
from repositories.taskRepository import TaskRepository
from repositories.userRepository import UserRepository
from services.login import Logger
from services.repositoriesService import RepositoriesService
from services.tasksService import TasksService
from services.usersService import UsersService

app = Flask(__name__)
app.register_error_handler(InvalidParameterException, lambda e: e)
app.register_error_handler(ItemNotFoundException, lambda e: e)
app.register_error_handler(MissingParameterException, lambda e: e)

CORS(app, supports_credentials=True)

git_repository = GitServerRepository()
user_repository = UserRepository(git_repository)
repository_repository = RepositoryRepository(user_repository, git_repository)
task_repository = TaskRepository(user_repository, repository_repository)

users_service = UsersService(user_repository, repository_repository)
repositories_service = RepositoriesService(repository_repository, git_repository, users_service)
tasks_service = TasksService(task_repository, users_service, repositories_service)
logger = Logger(user_repository)


@app.route('/')
def heartbeat():
    return 'Welcome to RePub API', 200


@app.route('/login', methods=['POST'])
def login():
    return_token = logger.log_user(request.get_json())
    return json.dumps(return_token), 200


@app.route('/logout', methods=['POST'])
def logout():
    logger.logout(request.headers.get("X-token-id"))
    return 'Logout successful', 200


@app.route('/signup', methods=['POST'])
def signup():
    result = users_service.create_user(request.get_json())
    return json.dumps({"userId": result}), 201


@app.route('/users', methods=['GET'])
def users():
    if request.args.get('filter') is not None:
        result = users_service.get_filtered_users(request.args.get('filter'))
        return json.dumps({"users": list(result), "total": len(result)}), 200
    result = users_service.get_all_users()
    return json.dumps({"users": list(result), "total": len(result)}), 200


@app.route('/users/<string:username>', methods=['GET', 'PUT', 'DELETE'])
def profile(username):
    if logger.check_if_token_is_valid(request.headers.get("X-token-id")) is False:
        print("Invalid token")
        return 'Invalid token', 401
    if request.method == 'GET':
        public = logger.get_user_by_token(request.headers.get("X-token-id")) != username
        print(public)
        result = users_service.get_user(username, public=public)
        return json.dumps(result), 200
    elif request.method == 'PUT':
        if logger.get_user_by_token(request.headers.get("X-token-id")) != username:
            return 'Unauthorized', 401
        users_service.update_user(username, request.get_json())
        return 'User with username {} updated'.format(username), 200
    elif request.method == 'DELETE':
        username_found = logger.get_user_by_token(request.headers.get("X-token-id"))
        print(username_found)
        if logger.get_user_by_token(request.headers.get("X-token-id")) != username:
            print("Invalid token here")
            return 'Unauthorized', 401
        users_service.delete_user(username)
        return 'User with username {} deleted'.format(username), 200
    else:
        return 'Method not allowed', 405


@app.route('/users/<string:username>/repositories', methods=['GET'])
def user_repositories(username):
    public = logger.get_user_by_token(request.headers.get("X-token-id")) != username
    result = repositories_service.get_user_repositories(username, public=public)
    return json.dumps({"repositories": list(result), "total": len(result)}, default=str), 200


@app.route('/users/<string:username>/tasks', methods=['GET'])
def user_tasks(username):
    result = tasks_service.get_user_tasks(username)
    return json.dumps({"tasks": list(result), "total": len(result)}, default=str), 200


@app.route('/users/<string:username>/repositories/<string:repository_name>', methods=['GET', 'PUT', 'DELETE'])
def repository(username, repository_name):
    if request.method == 'GET':
        result = repositories_service.get_repository(username, repository_name)
        return json.dumps(result), 200
    elif request.method == 'PUT':
        repositories_service.update_repository(username, repository_name, request.get_json())
        return f"Repository {username}/{repository_name} updated", 200
    elif request.method == 'DELETE':
        repositories_service.delete_repository(username, repository_name)
        return f"Repository {username}/{repository_name} deleted", 200
    else:
        return 'Method not allowed', 405


@app.route('/users/<string:username>/repositories/<string:repository_name>/branches', methods=['GET'])
def repository_branches(username, repository_name):
    result = repositories_service.get_repository_branches(username, repository_name)
    return json.dumps({"branches": result}, default=str), 200


@app.route('/users/<string:username>/repositories/<string:repository_name>/files', methods=['GET'])
def repository_files(username, repository_name):
    if request.args.get('path'):
        file_path = None
        try:
            file_path = repositories_service.get_file_content(username, repository_name, request.args.get('branch'),
                                                              request.args.get('path'))
            return send_file(file_path)
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
    else:
        result = repositories_service.get_user_repository_files(username, repository_name,
                                                                request.args.get('branch'))
        return json.dumps({"files": result}, default=str), 200


@app.route('/users/<string:username>/repositories/<string:repository_name>/tasks/<int:task_number>', methods=['GET'])
def specific_task_in_repository(username, repository_name, task_number):
    result = tasks_service.get_task_by_username_name_and_number(username, repository_name, task_number)
    return json.dumps(result, default=str), 200


@app.route('/repositories', methods=['GET', 'POST'])
def repositories():
    if request.method == 'GET':
        if request.args.get('filter'):
            result = repositories_service.get_repositories_by_filter(request.args.get('filter'))
            return json.dumps({"repositories": list(result), "total": len(result)}), 200
        result = repositories_service.get_public_repositories()
        return json.dumps({"repositories": list(result), "total": len(result)}), 200
    elif request.method == 'POST':
        result = repositories_service.create_repository(request.get_json())
        return json.dumps({"repository": result}), 201
    else:
        return 'Method not allowed', 405


@app.route('/users/<string:username>/repositories/<string:repository_name>/tasks', methods=['GET'])
def repository_issues(username, repository_name):
    result = tasks_service.get_repository_tasks(username, repository_name)
    return json.dumps({"tasks": list(result), "total": len(result)}, default=str), 200


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        result = tasks_service.get_all_tasks()
        return json.dumps({"tasks": list(result), "total": len(result)}, default=str), 200
    elif request.method == 'POST':
        result = tasks_service.create_task(request.get_json())
        return json.dumps({"taskId": result}), 201
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
    if request.method == 'GET':
        result = tasks_service.get_task_comments(task_id)
        return json.dumps({"comments": list(result), "total": len(result)}, default=str), 200
    elif request.method == 'POST':
        result = tasks_service.create_comment(task_id, request.get_json())
        return json.dumps({"commentId": result}), 201
    else:
        return 'Method not allowed', 405


@app.route('/comments/<int:comment_id>', methods=['GET', 'PUT', 'DELETE'])
def task_comment(comment_id):
    if request.method == 'GET':
        result = tasks_service.get_comment(comment_id)
        return json.dumps(result, default=str), 200
    elif request.method == 'PUT':
        tasks_service.update_comment(comment_id, request.get_json())
        return 'Comment with id {} updated'.format(comment_id), 200
    elif request.method == 'DELETE':
        tasks_service.delete_comment(comment_id)
        return 'Comment with id {} deleted'.format(comment_id), 200
    else:
        return 'Method not allowed', 405


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
