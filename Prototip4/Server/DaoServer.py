from dataclasses import dataclass, asdict
import mysql.connector
import hashlib
from time import time
import random
from typing import Optional, List, Dict


class UserDAO:

    def connectBBDD(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatapp"
        )
        return connection
     
    def getUserByToken(self, token: str) -> Optional[Dict]:
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = "SELECT * FROM User WHERE token = %s"
        cursor.execute(query, (token,))
        user = cursor.fetchone()
        cursor.close()
        con.close()
        return user


    def login(self, identifier: str, password: str) -> Optional[Dict]:
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = """
            SELECT * FROM User
            WHERE (username = %s OR email = %s) AND password = %s
        """
        cursor.execute(query, (identifier, identifier, password))
        user = cursor.fetchone()
        token = ""
        if user:
            token = self.setTokenUser(user['username'])
            user['token'] = token
        cursor.close()
        con.close()
        return user
    
    def setTokenUser(self, username: str) -> str:
        con = self.connectBBDD()
        cursor = con.cursor()
        token = self.getHash()
        query = "UPDATE User SET token = %s WHERE username = %s"
        cursor.execute(query, (token, username))
        con.commit()
        cursor.close()
        con.close()
        return token
    
    def getHash(self) -> str:
        milliseconds = str(time() * random.randrange(10000))
        data = milliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest()
    
    def getHash2(self, username: str) -> str:
        milliseconds = str(time() * 1000)
        data = username + milliseconds
        hash_object =  hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest()


class ChildDAO:

    def connectBBDD(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatapp"
        )
        return connection

    def getChilds(self, id_user: str) -> List[Dict]:
        con = self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        query = ("SELECT DISTINCT Child.* FROM RelationUserChild "
                 "JOIN Child ON RelationUserChild.child_id = Child.id "
                 "WHERE RelationUserChild.user_id = %s")
        cursor.execute(query, (id_user,))
        results = cursor.fetchall()
        cursor.close()
        con.close()
        return results
    
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
        return self.getTaps(user_id, child_id)


if __name__ == "__main__":
    dao = ChildDAO()
    user_id = 1
    child_id = 1
    result = dao.getTaps(user_id, child_id)
    print("RESULTADO TAPS:")
    print(result)
