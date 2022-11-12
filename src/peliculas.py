import csv
from ast import parse
from calendar import month
from collections import namedtuple, defaultdict
from datetime import datetime

from peliculas2 import *

Pelis = namedtuple("Pelis", "day, month, year, fecha, duration, title, subject, actor, actress, director, popularity, awards, rate")

def lee_datos(fichero):
    '''

    Devuelve una lista de tuplas de tipo Lista a partir de los datos incluidos en el fichero
    csv dado como parámetro. El fichero debe estar codificado en formato utf-8.
    Parametro: fichero. Nombre y ruta del fichero csv a leer. 
    Formato: fichero:srt
    Devuelve: Una lista de tuplas de tipo Lista con todos los datos del csv
    Formatos de la lista: [ Lista(str, str, str, datetime, int, str, str, str, str, str, int, boolean, float)]  
    
    '''
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
            peliculas.append(Pelis(day,month ,year, fecha ,duration, title, subject, actor, actress, director, popularity, awards, rate))

    return peliculas

def peliculas_leidas(fichero):
    '''
   A partir de un fichero csv, cuenta el número total de filas leidas (películas) y devuelve el número de películas leidas y las imprime enumeradas. 
   Parametro: fichero. Nombre y ruta del fichero csv a leer. 
   Formato: fichero:srt
   Devuelve: El número total de películas del csv, y un listado enumerado de ellas.
    '''
    numerototal = len(fichero)
    print(f"Se han leido {numerototal} películas")
    mostrar_numerado(fichero)

def tres_primeras_pelis(fichero):
    '''
    A partir de un fichero csv, imprime las tres primeras filas del csv, correspondientes a las tres primeras películas del csv.
    Parametro: fichero. Nombre y ruta del fichero csv a leer. 
    Formato: fichero:srt
    Devuelve: Las tres primeras listas de tuplas, correspondientes a las tres primeras películas
    '''
    
    print("Mostrando en pantalla las tres primeras películas:")
    mostrar_numerado(fichero[:3])

def tres_ultimas_pelis(fichero):
    '''
    A partir de un fichero csv, imprime las tres últimas filas del csv, correspondientes a las tres últimas películas del csv.
    Parametro: fichero. Nombre y ruta del fichero csv a leer. 
    Formato: fichero:srt
    Devuelve: Las tres primeras listas de tuplas, correspondientes a las tres primeras películas
    '''
    
    print("Mostrando en pantalla las tres últimas películas:")
    mostrar_numerado(fichero[-3:])

def filtra_por_categoria(fichero, categoria):
    '''
    B1
    A partir de un fichero csv y una categoría de película, devuelve todos los datos de todas las películas con dicha categoría
    '''
    return [tupla for tupla in fichero if tupla.subject == categoria]

def calcular_media_duracion_por_categoria(fichero, categoria):
    '''
    B1
    '''
    duraciones = [a.duration for a in fichero if a.subject == categoria]
    return sum(duraciones)/len(duraciones)

def ordenar_por_rating_y_anyo(fichero, anyo):
    '''
    B2 F2
    '''
    pe_lista = [(a.title, a.rate) for a in fichero if a.year == anyo]
    return sorted(pe_lista, key = lambda x:x[1], reverse = True)

def top_pelicula_por_categoria_y_anyo(fichero, anyo, categoria="Comedy"):
    '''
    B2 F1
    '''
    peliculas_por_categoria = filtra_por_categoria(fichero, categoria)
    pa = [e for e in peliculas_por_categoria if e.year == anyo]
    return max(pa, key = lambda x:x.rate)

def agrupar_por_categoria(fichero):
    res = defaultdict(str)
    for e in fichero:
        res[e.subject] += e.title + "; "
    return res