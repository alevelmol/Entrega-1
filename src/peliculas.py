from ast import parse
from calendar import month
from collections import namedtuple
import datetime
import csv

from peliculas2 import parse_bool

pelis = namedtuple("Lista", "day, month, year, duration, title, subject, actor, actress, director, popularity, awards, rate")

def lee_datos(fichero):
    peliculas = []
    with open(fichero, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter= ";")
        next (lector)
        for day, month, year, duration, title, subject, actor, actress, director, popularity, awards, rate in lector:
            day = int(day)
            month = int(month)
            year = int(year)
            duration = int(duration)
            popularity = int(popularity)
            awards = parse_bool(awards)
            rate = rate.replace("," , ".")
            rate = float(rate)
            peliculas.append(pelis(fecha ,duration, title, subject, actor, actress, director, popularity, awards, rate))

    return peliculas