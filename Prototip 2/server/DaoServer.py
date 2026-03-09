from flask import Flask, request, jsonify
from dadesserver import *

app = Flask(__name__)


class UserDAO:
    def __init__(self):
        self.users = users
        self.relation_user_child = relation_user_child

    def login(self, identifier, password):
        for u in self.users:
            if (u.username == identifier or u.email == identifier) and u.password == password:
                idrole = "2"  
                return {
                    "id": u.id,
                    "username": u.username,
                    "email": u.email,
                    "token": "token12345",
                    "idrole": idrole,
                    "msg": "Usuari Ok",
                    "coderesponse": "1"
                }
        return {"coderesponse": "0", "msg": "No validat"}

    def getUserById(self, user_id):
        for u in self.users:
            if u.id == user_id:
                return u
        return None


class ChildDAO:
    def __init__(self):
        self.childs = children
        self.relation_user_child = relation_user_child

    def getChildsByUser(self, user_id):
        child_ids = {r['child_id'] for r in self.relation_user_child if r['user_id'] == user_id}
        return [c.__dict__ for c in self.childs if c.id in child_ids]


class TapDAO:
    def __init__(self):
        self.taps = taps
        self.relation_user_child = relation_user_child

    def getTapsByUser(self, user_id):
        # Obtener IDs de children del user
        child_ids = {r['child_id'] for r in self.relation_user_child if r['user_id'] == user_id}
        return [t.__dict__ for t in self.taps if t.child_id in child_ids]

    def getTapsByChild(self, child_id):
        return [t.__dict__ for t in self.taps if t.child_id == child_id]




uDao = UserDAO()
cDao = ChildDAO()
tDao = TapDAO()




@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"coderesponse": "0", "msg": "No validat"}), 400

    response = uDao.login(data["username"], data["password"])
    status = 200 if response["coderesponse"] == "1" else 400
    return jsonify(response), status


@app.route("/child", methods=["POST"])
def child_service():
    data = request.get_json()
    if not data or "iduser" not in data:
        return jsonify({"msg": "Missing iduser", "coderesponse": "0", "data": []}), 400

    childs = cDao.getChildsByUser(data["iduser"])
    return jsonify({
        "msg": str(len(childs)),
        "coderesponse": "1",
        "data": childs
    })


@app.route("/tap", methods=["POST"])
def tap_service():
    data = request.get_json()
    if not data or "iduser" not in data:
        return jsonify({"msg": "Missing iduser", "coderesponse": "0", "data": []}), 400

    taps_list = tDao.getTapsByUser(data["iduser"])
    return jsonify({
        "msg": str(len(taps_list)),
        "coderesponse": "1",
        "data": taps_list
    })


if __name__ == "__main__":
    app.run(debug=True)