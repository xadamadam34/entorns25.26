from dataclasses import dataclass, asdict
from flask import jsonify
import mysql.connector
import hashlib
from time import time
import random


class UserDAO:

    def connectBBDD(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatapp"
        )
        return connection
     
    def getUserByToken(self,token):
        # connexió a BBDD
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = "SELECT * FROM User WHERE token = '" + token + "'"
        cursor.execute(query)
        user = cursor.fetchone()
        cursor.close()
        con.close()
        return user


    def login(self, identifier, password):
        # connexió a BBDD
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = """
            SELECT * FROM User
            WHERE (username = %s OR email = %s) AND password = %s
        """
        cursor.execute(query, (identifier, identifier, password))
        user = cursor.fetchone()
        token=""
        if user:
            token=self.setTokenUser(user['username'])
            #print(user)
            user['token']=token
        cursor.close()
        con.close()
        return user
    
    def setTokenUser(self, username):
        # connectar BBDD
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        # generar Token
        token=self.getHash() #token=self.getHash(username)
        # Update a BBDD camp Token al usuari per username
        print(type(token))
        query = "UPDATE User SET token ='" + token + "' WHERE username = '" + username +"'"
        # print(query)
        cursor.execute(query)
        con.commit()
        # Close BBDD
        cursor.close()
        con.close()
        return token
    
    def getHash(self):
        milliseconds = str(time() * random.randrange(10000))
        data=  milliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest() + ""
    
    def getHash2(self,username):
        milliseconds = str(time() * 1000)
        data=username + milliseconds
        hash_object =  hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest() + ""


class ChildDAO:

    def connectBBDD(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatapp"
        )
        return connection

    def getChilds(self,id_user):
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = "SELECT distinct  Child.* FROM RelationUserChild,Child WHERE RelationUserChild.user_id='"
        query += id_user + "' and RelationUserChild.child_id=Child.id"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        con.close()
        return  results
    
    def getTaps(self, user_id: int, child_id: int):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        query = """
            SELECT *
            FROM Tap
            WHERE user_id = %s AND child_id = %s
        """
        cursor.execute(query, (user_id, child_id))
        result = cursor.fetchall()
        cursor.close()
        con.close()
        
        return result
    
    def getTapByUserAndChild(self, user_id: int, child_id: int):
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)

        query = """
            SELECT *
            FROM Tap
            WHERE user_id = %s AND child_id = %s
        """

        cursor.execute(query, (user_id, child_id))
        result = cursor.fetchall()

        cursor.close()
        con.close()

        return result
    

if __name__ == "__main__":

        dao = ChildDAO()

        user_id = 1
        child_id = 1
        result = dao.getTaps(user_id, child_id)
        print("RESULTADO TAPS:")
        print(result)

    

        

'''
cdao=ChildDAO()
res=cdao.getChilds("1")
print(res)
dao=UserDAO()
u=dao.getUserByToken("5b8656c4f2dc8461550dc44543e4fdb23a481c1d76fcf2e1353fe5425f50ee40")
print(u)
u=dao.getUserByToken("123455")
print(u)
'''
