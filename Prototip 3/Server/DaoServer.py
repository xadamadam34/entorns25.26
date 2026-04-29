import hashlib
import random
from flask import Flask, request, jsonify
import mysql
from dadesServerr import *
import mysql.connector
from time import time
from dataclasses import dataclass, asdict


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
    
    def getUserByToken(self, token):
        # connexió a BBDD
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = "SELECT * FROM User WHERE token = %s"
        cursor.execute(query, (token,))
        user = cursor.fetchone()
        cursor.close()
        con.close()
        return user
    
    def getchilds(self, id_user):
        # connexió a BBDD
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = "SELECT * FROM Child WHERE id_user = " + str(id_user) 
        cursor.execute(query)
        childs = cursor.fetchall()
        cursor.close()
        con.close()
        return childs



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
        token = None
        if user:
           token = self.setTokenUser(user['username'])
           user['token'] = token
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
        query = "UPDATE User SET token = %s WHERE username = %s"
        cursor.execute(query, (token, username))
        con.commit()
        # Close connexió a BBDD
        cursor.close()
        con.close()
        return token


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
    
class ChildDAO:

    def connectBBDD(self):
        import mysql.connector
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatapp"
        )

    def getChilds(self, id_user):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        query = "SELECT * FROM Child WHERE id_user = %s"
        cursor.execute(query, (id_user,))

        childs = cursor.fetchall()

        cursor.close()
        con.close()

        return childs





dao = UserDAO()
u = dao.getUserByToken("b0a1c10c62c9aeebb7d7562b0b7ddb2b617793c16df0f96143a680193ac206f2")
print(u)

@dataclass
class ApiResponse():
    msg: str
    coderesponse: str
    data: list

# Instantiate DAO

userDao=UserDAO() 
childDao = ChildDAO()

@app.route('/login', methods=['POST'])
def login():
    user = None
    token = request.headers.get('api-token')
    if(token):
        # Validar token
        user = userDao.getUserByToken(token)
    else:
        # Existing username/password login
        data = request.get_json()
        identifier = data.get('username')  # username or email
        password = data.get('password')
        user = userDao.login(identifier, password)
    
    if user:
        response = ApiResponse(
            msg="Authenticated",
            coderesponse="1",
            data=user
        )
    else:
        response = ApiResponse(
            msg="Not authenticated",
            coderesponse="0",
            data=""
        )
    return jsonify(asdict(response)),200


@app.route('/child', methods=['POST'])
def child():
    token = request.headers.get('api-token')
    user = None
    if(token):
        # Validar token
        user = userDao.getUserByToken(token)

    if not user:
        response = ApiResponse(
            msg="Not authenticated",
            coderesponse="0",
            data=""
        )
        return jsonify(asdict(response)),401

    data = request.get_json()
    childs=childDao.getChilds(user['id'])
    response = ApiResponse(
            msg="Childs",
            coderesponse="1",
            data=childs
        )
    return jsonify(asdict(response)),200


if __name__ == '__main__':
    app.run(debug=True)