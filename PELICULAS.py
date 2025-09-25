from flask import Flask, jsonify
import random

app = Flask(__name__)


peliculas = [
    {
        "titulo": "El Exorcista",
        "director": "William Friedkin",
        "año": 1973,
        "sinopsis": "Una niña de doce años comienza a mostrar signos de posesión demoníaca, lo que lleva a sus padres a buscar ayuda de dos sacerdotes para realizar un exorcismo.",
        "calificacion": random.choice(["1 estrella", "2 estrellas", "3 estrellas"])
    },
    {
        "titulo": "Psicosis",
        "director": "Alfred Hitchcock",
        "año": 1960,
        "sinopsis": "Una secretaria roba dinero de su jefe y se refugia en un motel aislado regentado por un hombre con una personalidad perturbadora y su misteriosa madre.",
        "calificacion": random.choice(["1 estrella", "2 estrellas", "3 estrellas"])
    },
    {
        "titulo": "El Resplandor",
        "director": "Stanley Kubrick",
        "año": 1980,
        "sinopsis": "Un escritor acepta un trabajo como cuidador de un hotel aislado durante el invierno, pero el lugar comienza a desatar sus peores impulsos y locuras.",
        "calificacion": random.choice(["1 estrella", "2 estrellas", "3 estrellas"])
    },
    {
        "titulo": "La Cosa",
        "director": "John Carpenter",
        "año": 1982,
        "sinopsis": "Un equipo de investigadores en la Antártida descubre una criatura alienígena que puede imitar perfectamente a cualquier ser vivo, sembrando el pánico y la paranoia.",
        "calificacion": random.choice(["1 estrella", "2 estrellas", "3 estrellas"])
    },
    {
        "titulo": "Hereditary",
        "director": "Ari Aster",
        "año": 2018,
        "sinopsis": "Tras la muerte de su madre, una familia comienza a desentrañar secretos oscuros y fuerzas sobrenaturales que amenazan con destruirlos a todos.",
        "calificacion": random.choice(["1 estrella", "2 estrellas", "3 estrellas"])
    }
]

@app.route('/peliculas', methods=['GET'])
def obtener_peliculas():
    return jsonify(peliculas)

if __name__ == '__main__':
    app.run(debug=True)
