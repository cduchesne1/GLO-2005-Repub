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
