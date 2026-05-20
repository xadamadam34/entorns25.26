import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',       # Canvia per la teva contrasenya
        database='reserva_pistes'
    )
