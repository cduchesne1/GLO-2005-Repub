# GLO-2005
Semester project for the relational databses class.

## Frontend

To run the app:

`npm run serve`

## Backend

- Python 3.9

Create a virtual environment

Install dependencies from `requirements.txt`

To run the app (Make sure the database is up and running):
```bash
export FLASK_APP=hello
flask run
```

## Database

- Docker
- Docker Compose

To setup the database:

** Make sure that mysql is not running on port 3306 before starting the container **

1) Open a terminal in the `database` folder

2) Run the following command:
```bash
docker compose up
```

To stop the database, you can exit in the terminal with CTRL+C and run the following command:
```bash
docker compose down
```

## Git Server

- Docker
- Docker Compose

To setup the server for the first time:

1) Open a terminal in the `gitserver` folder

2) Run the following command:
```bash
docker compose build
docker compose up -d
```

3) Go in the `backend` folder and in the `util` folder.

4) Run the `getContainerId` python script to get the container id of the git server (make sure it is the only one running)

5) Copy the id into the .env file. The file should look like this:
```
GITSERVER_CONTAINER=thecontainerid
```

6) Run the `populateServer` python script to populate the repositories.

7) Steps 3 to 6 are only for the first time. You can start back the container manually or with the `docker compose up -d` after.

To stop the server, you can run the command:
```bash
docker compose down
```

### Clone a repository
To clone a repository run the following command:
```bash
git clone http://localhost:8000/username/repo.git
```
