from flask import Flask, request, jsonify
from dataclasses import dataclass, asdict

# Try relative import if used as package; otherwise rely on module in same folder.
try:
    from DaoServer import UserDAO, ChildDAO
except Exception:
    # when running as a package (python -m), try relative import
    try:
        from .DaoServer import UserDAO, ChildDAO
    except Exception:
        # last resort, adjust sys.path
        import os, sys
        sys.path.insert(0, os.path.dirname(__file__))
        from DaoServer import UserDAO, ChildDAO


@dataclass
class ApiResponse:
    msg: str
    coderesponse: str
    data: object = None


# Instantiate DAO
userDao = UserDAO()
childDao = ChildDAO()

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    # Token validation if exists
    token = request.headers.get("api-token")
    user = None
    if token:
        # comprobar que el token existe en un usuario
        user = userDao.getUserByToken(token)
    else:
        data = request.get_json() or {}
        identifier = data.get('username')  # username or email
        password = data.get('password')
        user = userDao.login(identifier, password)

    if user:
        response = ApiResponse(
            msg="Authenticated",
            coderesponse="1",
            data=user
        )
        return jsonify(asdict(response)), 200
    else:
        response = ApiResponse(
            msg="Not authenticated",
            coderesponse="0",
            data=""
        )
        return jsonify(asdict(response)), 400


@app.route('/child', methods=['POST'])
def child():
    token = request.headers.get("api-token")
    u = None
    if token:
        u = userDao.getUserByToken(token)

    if u:
        childs = childDao.getChilds(str(u['id']))
        response = ApiResponse(
            msg="GetChilds",
            coderesponse="1",
            data=childs
        )
        return jsonify(asdict(response)), 200
    else:
        response = ApiResponse(
            msg="Access not granted",
            coderesponse="0",
            data=""
        )
        return jsonify(asdict(response)), 400


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

    data = request.get_json() or {}
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
