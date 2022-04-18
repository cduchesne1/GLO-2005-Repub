import os

import docker
from dotenv import load_dotenv

from exceptions.ItemNotFoundException import ItemNotFoundException


class GitServerRepository:
    def __init__(self):
        load_dotenv()
        self.client = docker.from_env()
        self.container = self.client.containers.get(os.getenv('GITSERVER_CONTAINER'))

    def create_repository(self, username: str, repository_name: str) -> None:
        _, stream = self.container.exec_run(f"mkrepo {username} {repository_name}", stream=True)
        response = ""
        for data in stream:
            response += data.decode("utf-8")
        if "created" not in response:
            raise Exception("Error creating repository")

    def delete_repository(self, username: str, repository_name: str) -> None:
        _, stream = self.container.exec_run(f"rmrepo {username} {repository_name}", stream=True)
        response = ""
        for data in stream:
            response += data.decode("utf-8")

    def get_files(self, username: str, repository: str, branch: str) -> list[str]:
        _, stream = self.container.exec_run(f"lsfiles {username} {repository} {branch}", stream=True)
        files = []
        for data in stream:
            files = data.decode().split('\n')
        files.remove('')
        files = [] if len(files) == 1 and 'fatal' in files[0] else files
        return files

    def get_file_content(self, username: str, repository: str, branch: str, path: str) -> str:
        simple_path = path.split('/')[-1]
        file = open(f"temp/{simple_path}", "w")
        try:
            _, stream = self.container.exec_run(f"showcontent {username} {repository} {branch} {path}", stream=True)
            for data in stream:
                if 'fatal' in data.decode():
                    raise ItemNotFoundException(f"File {path} not found")
                file.write(data.decode())
            return f"temp/{simple_path}"
        finally:
            file.close()

    def get_branches(self, username: str, repository: str) -> list[str]:
        _, stream = self.container.exec_run(f"lsbranches {username} {repository}", stream=True)
        branches = []
        for data in stream:
            branches = data.decode().split('\n')
        branches.remove('') if '' in branches else None
        return branches
