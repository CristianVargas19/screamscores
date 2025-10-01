from flask import Flask, jsonify, render_template, request, redirect, url_for
import random
import json
import os

app = Flask(__name__)

# Archivo para guardar las reseñas
RESENAS_FILE = 'resenas.json'

# Datos de las películas de terror
peliculas = [
    {
        "id": 1,
        "titulo": "El Exorcista",
        "director": "William Friedkin",
        "año": 1973,
        "sinopsis": "Una niña de doce años comienza a mostrar signos de posesión demoníaca, lo que lleva a sus padres a buscar ayuda de dos sacerdotes para realizar un exorcismo.",
        "calificacion": random.choice(["1 estrella", "2 estrellas", "3 estrellas"])
    },
    {
        "id": 2,
        "titulo": "Psicosis",
        "director": "Alfred Hitchcock",
        "año": 1960,
        "sinopsis": "Una secretaria roba dinero de su jefe y se refugia en un motel aislado regentado por un hombre con una personalidad perturbadora y su misteriosa madre.",
        "calificacion": random.choice(["1 estrella", "2 estrellas", "3 estrellas"])
    },
    {
        "id": 3,
        "titulo": "El Resplandor",
        "director": "Stanley Kubrick",
        "año": 1980,
        "sinopsis": "Un escritor acepta un trabajo como cuidador de un hotel aislado durante el invierno, pero el lugar comienza a desatar sus peores impulsos y locuras.",
        "calificacion": random.choice(["1 estrella", "2 estrellas", "3 estrellas"])
    },
    {
        "id": 4,
        "titulo": "La Cosa",
        "director": "John Carpenter",
        "año": 1982,
        "sinopsis": "Un equipo de investigadores en la Antártida descubre una criatura alienígena que puede imitar perfectamente a cualquier ser vivo, sembrando el pánico y la paranoia.",
        "calificacion": random.choice(["1 estrella", "2 estrellas", "3 estrellas"])
    },
    {
        "id": 5,
        "titulo": "Hereditary",
        "director": "Ari Aster",
        "año": 2018,
        "sinopsis": "Tras la muerte de su madre, una familia comienza a desentrañar secretos oscuros y fuerzas sobrenaturales que amenazan con destruirlos a todos.",
        "calificacion": random.choice(["1 estrella", "2 estrellas", "3 estrellas"])
    }
]

def cargar_resenas():
    """Cargar reseñas desde el archivo JSON"""
    if os.path.exists(RESENAS_FILE):
        with open(RESENAS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_resenas(resenas):
    """Guardar reseñas en el archivo JSON"""
    with open(RESENAS_FILE, 'w', encoding='utf-8') as f:
        json.dump(resenas, f, ensure_ascii=False, indent=2)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/peliculas', methods=['GET'])
def obtener_peliculas():
    return jsonify(peliculas)

@app.route('/resenas', methods=['GET'])
def obtener_resenas():
    resenas = cargar_resenas()
    return jsonify(resenas)

@app.route('/agregar-resena', methods=['POST'])
def agregar_resena():
    try:
        data = request.get_json()
        
        nueva_resena = {
            "id": len(cargar_resenas()) + 1,
            "pelicula_id": data['pelicula_id'],
            "pelicula_titulo": data['pelicula_titulo'],
            "usuario": data['usuario'],
            "calificacion": data['calificacion'],
            "comentario": data['comentario'],
            "fecha": data['fecha']
        }
        
        resenas = cargar_resenas()
        resenas.append(nueva_resena)
        guardar_resenas(resenas)
        
        return jsonify({"mensaje": "Reseña agregada correctamente", "resena": nueva_resena}), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/info', methods=['GET'])
def info():
    estudiante = {
        "nombre": "Tu Nombre Completo",
        "matricula": "Tu Matrícula", 
        "curso": "Tecnologías de Construcción de Servicios Web"
    }
    return jsonify(estudiante)

if __name__ == '__main__':
    app.run(debug=True)