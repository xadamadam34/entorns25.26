from flask import Flask, jsonify, request

class User:
    def __init__(self,username, nom, password, email, rol="tutor"):
        self.username=username
        self.nom=nom
        self.password=password
        self.email=email
        self.rol=rol
    
    def __str__(self):
        return self.nom

#us1=User(username="ama",nom="Rob Halford",password="12345", email="rob@gmail.com",rol="tutor")
#print(us1)
users = [
    User(username="rob",nom="Rob Halford",password="12345", email="rob@gmail.com",rol="tutor"),
    User(username="john",nom="John Cannigan",password="12345", email="john@gmail.com",rol="tutor"),
    User(username="maria",nom="Maria Sams",password="12345", email="maria@gmail.com",rol="admin")
]

class UserDao:
    def __init__(self):
        self.users=users
    
    def getUserByUsername(self,uname):
        user = None
        for u in self.users:
            if u.username == uname:
                user = u.__dict__
        return user
    def getApellidoByUsername(self, uname):
        for u in self.users:
            if u.username == uname:
                return u.nom.split(" ")[1]  
    
    def getAllUsers(self):
        # Devuelve todos los usuarios como diccionarios
        return [u.__dict__ for u in self.users]
    
        return None
    def getAllUsernames(self):
        return [u.username for u in self.users]

# Test DAO
'''user_dao = UserDao()
response=user_dao.getUserByUsername("maria")
print(response)
response=user_dao.getUserByUsername("AAAA")
print(response) '''
# End TEST

# Instanciem el Dao User
user_dao = UserDao()

app = Flask(__name__)

@app.route('/user',methods=['GET'])
def user():
    resposta=""
    # Parametres
    username = request.args.get("username",default="")
    # Si els paràmetres OK
    if username != "":
        # Anar al DAO Server i cercar User per username
        resposta=user_dao.getUserByUsername(username)
        # respondre amb dades Ususari si trobat
        if resposta == None:
            resposta = {"msg":"Usuari No troba t"}
    else:  #  Si els paràmetres NO ok 
        # respondre error
        resposta = {"msg":"Falta paràmetre Username"}
    
    return jsonify(resposta)

@app.route('/usernames', methods=['GET'])
def usernames():
    usernames = user_dao.getAllUsernames()
    return jsonify(usernames)

@app.route('/allusernames', methods=['GET'])
def allusernames():
    all_users = user_dao.getAllUsers()
    return jsonify(all_users)




@app.route('/apellido', methods=['GET'])
def apellido():
    username = request.args.get("username")

    if not username:
        return jsonify({"msg": "Falta parámetro username"}), 400

    apellido = user_dao.getApellidoByUsername(username)

    if apellido is None:
        return jsonify({"msg": "Usuario no encontrado"}), 404

    return jsonify({"apellido": apellido})


class daoUserClient:
    def getUsernames(self):
        #Petició Http al WebService
        # TO-DO
        return None
    
class ViewConsole:
    def getInputUsername():
        # TO-DO
        return None
    def showUserInfo(user):
        # TO-DO
        return None
    
if __name__ == '__main__':
    app.run(debug=True)
