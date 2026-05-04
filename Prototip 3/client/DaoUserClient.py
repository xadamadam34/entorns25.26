import requests
from User import *
from flask import jsonify

class DaoUserClient:
    base_URL = "http://127.0.0.1:5000"
    token=""

    def login(self, user):
        # Validació paràmetres 
        # TO-DO
        # Petició HTTP al Webservice /login
        URL_peticio= self.base_URL + "/login"
        params_POST = {
            "username": user.username,
            "password": user.password
        }
        response = requests.post(URL_peticio, json=params_POST)
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response=user_data_raw['coderesponse']
            if code_response == '1': # Usuari Validat  (self, id, username, password, email, idrole,token):
                user_raw=user_data_raw['data']
                user=User(user_raw['id'], user_raw['username']
                          , "" ,user_raw['email']
                          , "", user_raw['token'])
                self.token=user_raw['token']
                return user
            else: 
                return None
        else:
            return None
    
    def loginToken(self, token):
        URL_peticio= self.base_URL + "/login"
        print(token)
        headers = {'Content-Type': 'application/json', 'api-token': token}
        response = requests.post(URL_peticio,headers=headers) 
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response=user_data_raw['coderesponse']
            if code_response == '1': # Usuari Validat  (self, id, username, password, email, idrole,token):
                user_raw=user_data_raw['data']
                user=User(user_raw['id'], user_raw['username']
                          , "" ,user_raw['email']
                          , "", user_raw['token'])
                return user  
        else:
            return None

    def childToken(self, token):
        URL_peticio= self.base_URL + "/child"
        #print(token)
        headers = {'Content-Type': 'application/json', 'api-token': token}
        response = requests.post(URL_peticio,headers=headers) 
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response=user_data_raw['coderesponse']
            if code_response == '1': # Usuari Validat  (self, id, username, password, email, idrole,token):
                user_raw=user_data_raw['data']
                print("type user_raw child/: ", type(user_raw))
                return user_raw
        else:
            return None


daoClient=DaoUserClient()

#resposta=daoClient.loginToken("20732fb71deb93f1ec163dc3b03aaafddfff76ccfdf45150e94d01eb099eb651")
#print(resposta)

#user=User("","mare", "mare", "12345", "", "")
#resposta=daoClient.login(user)
#print(resposta)
#print(daoClient.token)
resposta=daoClient.childToken("b1b901174df1095c12afb6b5429f3cdc4eb6c437a165a8f6426fb5d9330edaad")
print(resposta)


'''Servei Login
End-point: /login
Method: POST
Estat: Public
Tipus petició : application/json
Paramètres:

username : (string) username o email
password : (string) password
Resposta Usuari validat Ok:
http Response Code: 200 ok

{
  "coderesponse": "1",
  "data": {
    "email": "prova@gmail.com",
    "id": 1,
    "idrole": 1,
    "password": "12345",
    "token": "",
    "username": "mare"
  },
  "msg": "Authenticated"
}
Resposta Usuari No validat: http Response Code: 400 ok

{
     "coderesponse": "0"
     "msg": "No validat"
}
'''
