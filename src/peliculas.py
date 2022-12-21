import csv
from ast import parse
from calendar import month
from collections import namedtuple, defaultdict, OrderedDict
from datetime import datetime
from matplotlib import pyplot as plt

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
def top_pelicula_por_categoria_y_anyo(fichero):
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
    anyos = {p.year for p in fichero}
    peliculas = [e for e in fichero]
    pa = [e for e in peliculas if e.year == min(anyos)]
    return pa

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
    res = dict()
    
    for e in fichero:
        clave = e.subject
        if clave not in res:
            res[clave] = [e]
        else:
            res[e.subject].append(e)
    return res

def contar_peliculas_por_anyo(fichero):
    """
    B3 F1 (8)
    A partir de un fichero CSV, devuelve un diccionario que cuenta las peliculas que hay por cada año
    Parametros: fichero: Nombre y ruta del fichero csv a leer.
    Formato: fichero:str
    Devuelve: Un diccionario cuyas claves son los años y los valores, las peliculas estrenadas en dicho año
    """
    d = defaultdict(int)
    for p in fichero:
        d[p.year] += 1
    return d

def pelicula_con_mas_duracion(fichero):
    """
    B3 F2 (11)
    A partir de un fichero CSV, devuelve una tupla con el titulo y la duracion de la pelicula mas larga del dataset
    Parametros: fichero: Nombre y ruta del fichero csv a leer.
    Formato: fichero:str
    Devuelve: Una tupla conformada por el titulo de la pelicula y su duracion, en minutos
    """
    d = defaultdict()
    for p in fichero:
        d[p.title] = p.duration

    return max(d.items(), key = lambda x:x[1])


def aux_dic(fichero):
    """
    AUX PARA B3 F3 (12)
    A partir de un fichero CSV, devuelve una lista de tuplas conformadas por una tupla, que contiene el titulo y año de la pelicula, y otra que contiene la valoracion de la misma, ordenadas todas de mayor a menor por valoracion
    Parametros: fichero: Nombre y ruta del fichero csv a leer.
    Formato: fichero:str
    Devuelve: Una lista de tuplas conformadas por una tupla con titulo y año, y la valoracion de la pelicula
    """
    d = defaultdict()
    for p in fichero:
        d[(p.title, p.year)] = p.rate
    return sorted(d.items(), key = lambda x:x[1], reverse = True)
def pelicula_con_mas_valoracion_por_anyo(fichero):
    """
    B3 F3 (12)
    A partir de un fichero CSV y una funcion auxiliar, devuelve la pelicula con más valoracion por cada año
    Parametros: fichero: Nombre y ruta del fichero csv a leer.
    Formato: fichero:str
    Devuelve: Un diccionario cuyas claves son los años y los valores son el titulo de la pelicula y su correspondiente valoracion.
    """
    d = defaultdict(list)
    for titan, pel in aux_dic(fichero):
        d[titan[1]] += [(titan[0], pel)]
    return {an : m[0] for an, m in d.items()}

def aux_dic_2(fichero):
    """
    AUX PARA B3 F4 (14)
    A partir de un fichero CSV, devuelve una lista de tuplas conformadas por una tupla, que contiene el titulo y genero de la pelicula, y otra que contiene la valoracion de la misma, ordenadas todas de mayor a menor por valoracion
    Parametros: fichero: Nombre y ruta del fichero csv a leer.
    Formato: fichero:str
    Devuelve: Una lista de tuplas conformadas por una tupla con titulo y genero, y la valoracion de la pelicula
    """
    d = defaultdict()
    for p in fichero:
        d[(p.title, p.subject)] = p.rate
    return sorted(d.items(), key = lambda x:x[1], reverse = True)

def top_n_peliculas_por_genero(fichero, n=3):
    """
    B3 F4 (14)
    A partir de un fichero CSV y una funcion auxiliar, devuelve el top n de peliculas con mas valoracion por genero
    Parametros: fichero: Nombre y ruta del fichero csv a leer.
    Formato: fichero:str
    Devuelve: Un diccionario cuyas claves son los generos y los valores son el titulo de la pelicula y su correspondiente valoracion.
    """
    d = defaultdict(list)
    for titan, pel in aux_dic_2(fichero):
        d[titan[1]] += [(titan[0], pel)]
    return {an : m[:n] for an, m in d.items()}

def tabla_generos(fichero):
    """
    B4 F1
    A partir de un fichero CSV, devuelve un gráfico de barras donde por cada genero, indica el numero de peliculas con ese genero
    Parametros: fichero: Nombre y ruta del fichero csv a leer.
    Formato: fichero:str
    Devuelve: Un grafico cuyo eje x son los generos y cuyo eje y son las peliculas con dicho genero
    """
    d = defaultdict(int)
    for p in fichero:
        d[p.subject] += 1
    info = d.items()
    generos = [a[0] for a in info]
    num = [a[1] for a in info]
    plt.bar(generos, num, width=0.7, edgecolor="black" ,color = ["red", "darkorange", "gold", "yellow", "lime", "cyan", "steelblue", "blueviolet", "deeppink"])
    plt.title("Grafica generos")
    plt.show()
    

def dic_mes_sumvaloraciones(fichero):
    d = defaultdict(int)
    for e in fichero:
        d[e.month] += e.rate
        
    return d