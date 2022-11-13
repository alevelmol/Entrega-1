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

def filtra_por_categoria(fichero, categoria):
    '''
    B1 F1
    A partir de un fichero csv y una categoría de película, devuelve todos los datos de todas las películas con dicha categoría
    Parametros: fichero: Nombre y ruta del fichero csv a leer.
                categoria: Nombre de la categoria a filtrar
    Formato: fichero:str
             categoria:str
    Devuelve: Las listas de tuplas, correspondientes a todas las películas de la categoria introducida
    '''
    return [tupla for tupla in fichero if tupla.subject == categoria]

def calcular_media_duracion_por_categoria(fichero, categoria):
    '''
    B1 F2
    A partir de un fichero csv y una categoría de película, devuelve la media de duraciones de todas las peliculas con dicha categoría
    Parametros: fichero: Nombre y ruta del fichero csv a leer.
                categoria: Nombre de la categoria a filtrar
    Formato: fichero:str
             categoria:str
    Devuelve: Un valor float, correspondiente a la media de las duraciones de las películas de la categoría indicada.
    '''
    duraciones = [a.duration for a in fichero if a.subject == categoria]
    return sum(duraciones)/len(duraciones)
def top_pelicula_por_categoria_y_anyo(fichero, anyo, categoria="Comedy"):
    '''
    B2 F1
    A partir de un fichero csv, un año concreto y una categoría de película, la cual tiene como valor predeterminado "Comedy", devuelve la mejor pelicula en cuestion de la valoracion cuyo año y categoria son los indicados en la función.
    Parametros: fichero: Nombre y ruta del fichero csv a leer.
                anyo: Año de lanzamiento de las películas a filtrar
                categoria: Nombre de la categoria a filtrar (Valor predeterminado = "Comedy")
    Formato: fichero:str
             anyo:str
             categoria:str
    Devuelve: La tupla correspondiente a la mejor pelicula del año y categoria indicados
    '''
    peliculas_por_categoria = filtra_por_categoria(fichero, categoria)
    pa = [e for e in peliculas_por_categoria if e.year == anyo]
    return max(pa, key = lambda x:x.rate)

def ordenar_por_rating_y_anyo(fichero, anyo):
    '''
    B2 F2
    A partir de un fichero csv y un año concreto, devuelve una lista de tuplas con el título y la valoracion de cada pelicula cuyo año de lanzamiento es el indicado en la función
    Parametros: fichero: Nombre y ruta del fichero csv a leer.
                anyo: Año de lanzamiento de las películas a filtrar
    Formato: fichero:str
             anyo:str
    Devuelve: Una lista de tuplas,con el titulo y la valoración de la pelicula, ordenadas de mayor a menor valoracion, del año introducido en la funcion.
    '''
    pe_lista = [(a.title, a.rate) for a in fichero if a.year == anyo]
    return sorted(pe_lista, key = lambda x:x[1], reverse = True)


def agrupar_por_categoria(fichero):
    '''
    B2 F3
    A partir de un fichero csv, devuelve un diccionario en el que las peliculas se agrupan por categoria.
    Parametros: fichero: Nombre y ruta del fichero csv a leer.
    Formato: fichero:str
    Devuelve: Un diccionario cuyas claves son las diferentes categorias de las peliculas, y los valores, aquellas películas que tengan dicha categoria
    '''
    res = defaultdict(str)
    for e in fichero:
        res[e.subject] += e.title + "; "
    return res