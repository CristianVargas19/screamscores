from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Film(BaseModel):
    id: int
    title: str
    synopsis: str
    year: int
    ratings_1_star: int
    ratings_2_stars: int
    ratings_3_stars: int

# Datos de pelicula 1
films_db = [
    film(
        id=1,
        title="The Conjuring: Last Rites",
        synopsis="In 1986 paranormal investigators Ed and Lorraine Warren travel to Pennsylvania to vanquish a demon from a family's home.",
        year=2025,
        ratings_1_star=0,
        ratings_2_stars=1,
        ratings_3_stars=0

    ),
    film(
        id=2,
        title="El Resplandor",
        synopsis="Un hombre se vuelve loco en un hotel aislado durante el invierno.",
        year=1980,
        ratings_1_star=0,
        ratings_2_stars=0,
        ratings_3_stars=25
    )
]

@app.get("/films", response_model=List[films])
def get_films():
    return films_db

@app.get("/films/{film_id}", response_model=film)
def get_film(film_id: int):
    for film in films_db:
        if film.id == film_id:
            return film
    return {"error": "Film not found"}