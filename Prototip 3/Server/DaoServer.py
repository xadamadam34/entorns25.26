import hashlib
import random
import token
from flask import Flask, request, jsonify
import mysql
from dadesServerr import *
import mysql.connector
from time import time

app = Flask(__name__)


class UserDAO:
       

    def connectBBDD(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatapp"
        )
        return connection       

    def login(self, identifier, password):
        # connexió a BBDD
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = """
          SELECT * FROM User
          WHERE (username = %s OR email = %s) AND password = %s
          """
        cursor.execute(query, (identifier, identifier, password))
        user = cursor.fetchone()
        if user:
           self.setTokenUser(user['username'])
        print
        user ['token'] = token
        cursor.close()
        con.close()
        return user
    
    def setTokenUser(self, username):
        # connexió a BBDD
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        # Generar un token
        token = self.getHash(username)
        # update del token a la BBDD
        print (type(token))
        query = " UPDATE User SET token = '" + token + "' Where username = '" + username + "'"
        print(query)
        cursor.execute(query)
        con.commit()
        # Close connexió a BBDD
        cursor.close()
        con.close()


    def getHash2(self, username):
        miliseconds = str(time() * 1000)
        data = username + (miliseconds)
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest()
    
    def getHash(self, username):
        miliseconds = str(time() * random.randrange(1000))
        data = username + (miliseconds)
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest() + ""


        


dao=UserDAO()
u=dao.login("mare", "mare")
print(u)


