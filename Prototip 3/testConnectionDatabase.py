import mysql.connector

def list_users():
    """
    Connects to the MySQL database and lists all rows in the User table.
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="tapatappdam1"
    )
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM User"
        cursor.execute(query)
        users = cursor.fetchall()

        for user in users:
            print(user)
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    list_users()
