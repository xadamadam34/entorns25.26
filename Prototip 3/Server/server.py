from flask import Flask, request, jsonify
from DaoServer import UserDAO,ChildDAO
from dataclasses import dataclass, asdict

@dataclass
class ApiResponse():
    msg: str
    coderesponse: str
    data: list

# Instantiate DAO
userDao=UserDAO()
childDao=ChildDAO()

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Token validation if exists
    #print(request.headers)
    token=request.headers.get("api-token")
    #print("Token:" , token)
    user=None
    if(token):
        # comprovar que el token existeix a un usuari
        user=userDao.getUserByToken(token)
    else:
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
    token=request.headers.get("api-token")
    u=None
    if(token):
        # comprovar que el token existeix a un usuari
        print(token)
        u=userDao.getUserByToken(token)
        print("USER:", u)
    
    if u:
        #data = request.get_json()
        childs=childDao.getChilds(str(u['id']))
        response = ApiResponse(
                msg="GetChilds",
                coderesponse="1",
                data=childs
            )
        return jsonify(asdict(response)),200
    else: 
        response = ApiResponse(
            msg="Acces not granted",
            coderesponse="0",
            data=""
        )
        return jsonify(asdict(response)),400
    
@app.route('/taps', methods=['POST'])
def taps():
    token = request.headers.get("api-token")

    u = None
    if token:
        u = userDao.getUserByToken(token)

    if not u:
        response = ApiResponse(
            msg="Access not granted",
            coderesponse="0",
            data=""
        )
        return jsonify(asdict(response)), 400

    data = request.get_json()
    child_id = data.get("child_id")

    taps = childDao.getTaps(u['id'], child_id)

    response = ApiResponse(
        msg="Get Taps",
        coderesponse="1",
        data=taps
    )

    return jsonify(asdict(response)), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
