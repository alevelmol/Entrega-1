from ast import parse
from calendar import month
from collections import namedtuple
from datetime import datetime
import csv

from peliculas2 import *

pelis = namedtuple("Lista", "day, month, year, fecha, duration, title, subject, actor, actress, director, popularity, awards, rate")

def lee_datos(fichero):
    peliculas = []
    with open(fichero, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter= ";")
        next (lector)
        for day, month, year, duration, title, subject, actor, actress, director, popularity, awards, rate in lector:
            fecha = day +"-"+ month +"-"+ year
            fecha = datetime.strptime(fecha , "%d-%m-%Y").date()
            duration = parse_int(duration)
            popularity = parse_int(popularity)
            awards = parse_bool(awards)
            rate = rate.replace("," , ".")
            rate = parse_float(rate)
            peliculas.append(pelis(day,month ,year, fecha ,duration, title, subject, actor, actress, director, popularity, awards, rate))

    return peliculas

def peliculas_leidas(fichero):
    numerototal = len(fichero)
    print(f"Se han leido {numerototal} películas")
    mostrar_numerado(fichero)

def tres_primeras_pelis(fichero):
    print("Mostrando en pantalla las tres primeras películas:")
    mostrar_numerado(fichero[:3])

def tres_ultimas_pelis(fichero):
    print("Mostrando en pantalla las tres últimas películas:")
    mostrar_numerado(fichero[-3:])