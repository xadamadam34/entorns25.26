from flask import Flask, request, jsonify
from DaoServer import UserDAO
from dataclasses import dataclass, asdict

@dataclass
class ApiResponse():
    msg: str
    coderesponse: str
    data: list

# Instantiate DAO
userDao=UserDAO()

app = Flask(__name__)

@app.route('/getusers', methods=['GET'])
def getusers():
    response = ApiResponse(
        msg="All Users",
        coderesponse="1",
        data=userDao.getAllUsers()
    )
    return jsonify(asdict(response)),200


@app.route('/login', methods=['POST'])
def login():
    # Existing username/password login
    data = request.get_json()
    identifier = data.get('username')  # username or email
    password = data.get('password')
    user = userDao.login(identifier, password)
    response = ApiResponse(
            msg="login",
            coderesponse="-1",
            data=user
        )
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
