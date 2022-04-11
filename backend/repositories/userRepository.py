import bcrypt
import pymysql

connection = pymysql.connect(host='localhost', user='user', password='password', db='mydb')
cursor = connection.cursor()


def __to_dto(row):
    return {
        "id": row[0],
        "name": row[1],
        "username": row[2],
        "email": row[3],
        "bio": row[4],
        "website": row[5],
        "company": row[6],
        "location": row[7],
    }


def get_all_users():
    cursor.execute("SELECT * FROM users;")
    result = cursor.fetchall()
    return [__to_dto(row) for row in result]


def create_user(user_data):
    cursor.execute(
        "INSERT INTO users (name, username, email, bio, website, company, location) VALUES (%s, %s, %s, NULL, NULL, NULL, NULL);",
        (user_data['name'], user_data['username'], user_data['email']))
    cursor.execute("INSERT INTO authentication (id, password) VALUES (%s, %s);",
                   (cursor.lastrowid, __encrypt_password(user_data['password'])))
    connection.commit()
    return cursor.lastrowid


def __encrypt_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
    result = cursor.fetchone()
    return __to_dto(result) if result else None


def update_user(user_id, user_data):
    cursor.execute(
        "UPDATE users SET name = %s, username = %s, email = %s, bio = %s, website = %s, company = %s, location = %s WHERE id = %s;",
        (user_data["name"], user_data["username"], user_data["email"], user_data["bio"], user_data["website"],
         user_data["company"], user_data["location"], user_id))
    connection.commit()


def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
    connection.commit()


def username_exists(username):
    cursor.execute("SELECT * FROM users WHERE username = %s;", username)
    return cursor.fetchone() is not None


def email_exists(email):
    cursor.execute("SELECT * FROM users WHERE email = %s;", email)
    return cursor.fetchone() is not None

def log_user(user_credential):
    pass