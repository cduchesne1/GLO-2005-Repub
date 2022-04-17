import docker

client = docker.from_env()

if __name__ == "__main__":
    # Make sure the only container running is the one we want
    print(client.containers.list())
