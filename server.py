from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hola_mundo():
    nombre = "Cinéfilo"  # Reemplaza con tu nombre real
    return f"Hola, {nombre}"

@app.route('/api/info', methods=['GET'])
def info():
    estudiante = {
        "nombre": "Tu Nombre Completo",
        "matricula": "Tu Matrícula",
        "curso": "Tecnologías de Construcción de Servicios Web"
    }
    return jsonify(estudiante)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)