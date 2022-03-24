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
