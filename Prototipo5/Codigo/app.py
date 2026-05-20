from flask import Flask, request, jsonify
from flask_cors import CORS
from dao.usuari_dao import UsuariDAO
from dao.pista_dao import PistaDAO
from dao.reserva_dao import ReservaDAO
from dao.schedule_dao import ScheduleDAO
from dao.centre_dao import CentreDAO

app = Flask(__name__)
CORS(app)

# ──────────────────────────────────────────
# USUARIS
# ──────────────────────────────────────────

@app.route('/api/registre', methods=['POST'])
def registre():
    data = request.get_json()
    nom = data.get('nom')
    email = data.get('email')
    password = data.get('password')

    if not nom or not email or not password:
        return jsonify({'error': 'Falten camps obligatoris'}), 400

    dao = UsuariDAO()
    resultat = dao.crear_usuari(nom, email, password)
    if resultat:
        return jsonify({'missatge': 'Usuari registrat correctament'}), 201
    else:
        return jsonify({'error': 'El correu ja existeix'}), 409


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    dao = UsuariDAO()
    usuari = dao.verificar_usuari(email, password)
    if usuari:
        return jsonify({'missatge': 'Login correcte', 'usuari': usuari}), 200
    else:
        return jsonify({'error': 'Credencials incorrectes'}), 401


# ──────────────────────────────────────────
# CENTRES
# ──────────────────────────────────────────

@app.route('/api/centres', methods=['GET'])
def obtenir_centres():
    dao = CentreDAO()
    centres = dao.obtenir_tots()
    return jsonify(centres), 200


# ──────────────────────────────────────────
# PISTES
# ──────────────────────────────────────────

@app.route('/api/pistes', methods=['GET'])
def obtenir_pistes():
    dao = PistaDAO()
    pistes = dao.obtenir_totes()
    return jsonify(pistes), 200


@app.route('/api/pistes/<int:id_pista>', methods=['GET'])
def obtenir_pista(id_pista):
    dao = PistaDAO()
    pista = dao.obtenir_per_id(id_pista)
    if pista:
        return jsonify(pista), 200
    return jsonify({'error': 'Pista no trobada'}), 404


# ──────────────────────────────────────────
# SCHEDULES
# ──────────────────────────────────────────

@app.route('/api/schedules/pista/<int:id_pista>', methods=['GET'])
def obtenir_schedules(id_pista):
    dao = ScheduleDAO()
    schedules = dao.obtenir_per_pista(id_pista)
    return jsonify(schedules), 200


# ──────────────────────────────────────────
# RESERVES
# ──────────────────────────────────────────

@app.route('/api/reserves', methods=['POST'])
def crear_reserva():
    data = request.get_json()
    id_usuari   = data.get('id_usuari')
    id_schedule = data.get('id_schedule')

    if not id_usuari or not id_schedule:
        return jsonify({'error': 'Falten camps obligatoris'}), 400

    dao = ReservaDAO()
    resultat = dao.crear_reserva(id_usuari, id_schedule)
    if resultat:
        return jsonify({'missatge': 'Reserva creada correctament'}), 201
    else:
        return jsonify({'error': 'Aquest horari ja està reservat'}), 409


@app.route('/api/reserves/usuari/<int:id_usuari>', methods=['GET'])
def reserves_usuari(id_usuari):
    dao = ReservaDAO()
    reserves = dao.obtenir_per_usuari(id_usuari)
    return jsonify(reserves), 200


@app.route('/api/reserves/<int:id_reserva>', methods=['DELETE'])
def cancel_lar_reserva(id_reserva):
    dao = ReservaDAO()
    resultat = dao.eliminar_reserva(id_reserva)
    if resultat:
        return jsonify({'missatge': 'Reserva cancel·lada correctament'}), 200
    return jsonify({'error': 'Reserva no trobada'}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)
