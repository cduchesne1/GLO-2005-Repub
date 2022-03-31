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
    try:
        cursor.execute("SELECT * FROM users;")
        result = cursor.fetchall()
        return [__to_dto(row) for row in result]
    except Exception as e:
        print(e)
        return None


def get_user(user_id):
    try:
        cursor.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
        result = cursor.fetchone()
        return __to_dto(result)
    except Exception as e:
        print(e)
        return None


def update_user(user_id, user_data):
    try:
        cursor.execute("UPDATE users SET name = %s, username = %s, email = %s, bio = %s, website = %s, company = %s, location = %s WHERE id = %s;",
                       (user_data["name"], user_data["username"], user_data["email"], user_data["bio"], user_data["website"], user_data["company"], user_data["location"], user_id))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False


def delete_user(user_id):
    try:
        cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False