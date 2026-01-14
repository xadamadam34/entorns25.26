from flask import Flask, request, jsonify


app = Flask(__name__)


# --- Ruta GET ---
# Ejemplo: http://localhost:5000/saludo?nombre=Juan
@app.route('/saludo', methods=['GET'])
def saludo():
    nombre = request.args.get('nombre')  # Parámetro en la URL
    if not nombre:
        return jsonify({'error': 'Falta el parámetro "nombre"'}), 400
    return jsonify({'mensaje': f'Hola, {nombre}!'})




# --- Ruta POST ---
# Ejemplo: POST a http://localhost:5000/sumar con body JSON {"numero": 5}
@app.route('/sumar', methods=['POST'])
def sumar():
    data = request.get_json() or request.form  # Soporta JSON y form-data
    numero = data.get('numero')
    if numero is None:
        return jsonify({'error': 'Falta el parámetro "numero"'}), 400
    try:
        resultado = int(numero) + 10
    except ValueError:
        return jsonify({'error': '"numero" debe ser un entero'}), 400
    return jsonify({'resultado': resultado})




if __name__ == '__main__':
    app.run(debug=True)