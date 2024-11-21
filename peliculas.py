from fastapi import APIRouter, Path
from model import Pelicula

lista_peliculas = []
pelicula = APIRouter()

@pelicula.post("/peliculas")
def add_todo(todo:dict):
    lista_peliculas.append(todo)
    return {"message":"Added"}

@pelicula.get("/peliculas")
def show_peliculas():
    return {"peliculas":lista_peliculas}

@pelicula.get("/peliculas/{id_pelicula}")
def  show_one_todo(id_pelicula: int=Path(...,title="ID")):
    for pelicula in lista_peliculas:
        if pelicula["id"] == id_pelicula:
            return { "Pelicula":pelicula }
    return {"message": "ID doesn't exist"}