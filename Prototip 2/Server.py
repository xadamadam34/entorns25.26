from flask import Flask, jsonify, request
from dataclasses import dataclass, asdict

app = Flask(__name__)

# -------------------------
# DATOS EN MEMORIA
# -------------------------
# Simulando users y children
class User:
    def __init__(self, id, username, password, email, idrole=1, token=""):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.idrole = idrole
        self.token = token

class Child:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Datos de prueba
users = [
    User(1,"rob","12345","rob@gmail.com"),
    User(2,"john","12345","john@gmail.com")
]

children = [
    Child(1,"Pedro"),
    Child(2,"Ana"),
    Child(3,"Luis")
]

relation_user_child = [
    {"user_id": 1, "child_id": 1},
    {"user_id": 1, "child_id": 2},
    {"user_id": 2, "child_id": 3}
]

# -------------------------
# DAO
# -------------------------
class UserDAO:
    def __init__(self):
        self.users = users

    def getAllUsers(self):
        return [user.__dict__ for user in self.users]

    def getUserByUsername(self, username):
        for user in self.users:
            if user.username == username:
                return user.__dict__
        return None
    
    def login(self, identifier, password):
        for user in self.users:
            if (user.username == identifier or user.email == identifier) and user.password == password:
                return user.__dict__
        return None

class ChildDAO:
    def __init__(self):
        self.childs = children
        self.relation_user_child = relation_user_child

    def getChilds(self, user): 
        # Get IDs from relations
        child_ids = {r['child_id'] for r in self.relation_user_child if r['user_id'] == user.id}
        # Return Child objects
        return [c.__dict__ for c in self.childs if c.id in child_ids]

# Instancias
user_dao = UserDAO()
child_dao = ChildDAO()

# -------------------------
# RUTAS WEB
# -------------------------
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(user_dao.getAllUsers())

@app.route('/user', methods=['GET'])
def get_user_by_username():
    username = request.args.get("username", default="")
    if username:
        user = user_dao.getUserByUsername(username)
        if user:
            return jsonify(user)
        return jsonify({"msg":"Usuario no encontrado"}), 404
    return jsonify({"msg":"Falta parámetro username"}), 400

@app.route('/children_by_user', methods=['GET'])
def get_children_by_user():
    username = request.args.get("username", default="")
    if username:
        user_dict = user_dao.getUserByUsername(username)
        if not user_dict:
            return jsonify({"msg":"Usuario no encontrado"}), 404
        # Crear objeto User para DAO
        u = User(**user_dict)
        childs = child_dao.getChilds(u)
        return jsonify(childs)
    return jsonify({"msg":"Falta parámetro username"}), 400

@app.route('/allchildren', methods=['GET'])
def get_all_children():
    # Para listar todos los hijos
    return jsonify([c.__dict__ for c in children])

# -------------------------
# INICIO SERVIDOR
# -------------------------
if __name__ == '__main__':
    app.run(debug=True)
