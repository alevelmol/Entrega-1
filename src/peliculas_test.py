


from peliculas import *
from peliculas2 import mostrar_numerado


def test_lee_datos(fichero):
    
    PELIS = lee_datos("Entrega 1\data\movie_dataset.csv")
    #print(PELIS)
    print(f"Han sido leidos {len(PELIS)} datos")
    print(f"Las tres primeras peliculas son: {PELIS[:3]}")
    print(f"Las tres ultimas peliculas son: {PELIS[-3:]}")

def test_filtra_por_categoria(fichero):
    categoria = "Comedy"
    print(f"Las películas con la categoria {categoria} son:")
    mostrar_numerado(filtra_por_categoria(fichero, categoria))
def test_calcular_media_duracion_por_categoria(fichero):
    categoria = "Comedy"
    print(f"La media de las duraciones de las películas de la categoría {categoria} es: ")
    print(calcular_media_duracion_por_categoria(fichero, categoria))

def test_top_pelicula_por_categoria_y_anyo(fichero):
    #anyo = "1985"
    #categoria = "Drama"
    a = top_pelicula_por_categoria_y_anyo(fichero)
    print(f"La pelicula mas antigua es {a}")

def test_ordenar_por_rating_y_anyo(fichero):
    anyo = "1957"
    a = ordenar_por_rating_y_anyo(fichero, anyo)
    print(f"Las peliculas del anyo {anyo}, ordenadas por puntaje son: {a}")

def test_agrupar_por_categoria(fichero):
    a = agrupar_por_categoria(fichero)
    #print (a)
    for k,v in a.items():
        print(f"{k} ----> {v}")

def test_contar_peliculas_por_anyo(fichero):
    a = contar_peliculas_por_anyo(fichero)
    for k,v in a.items():
        print(f"{k} ----> {v}")

def test_pelicula_con_mas_duracion(fichero):
    print(f"La pelicula con más duracion es {pelicula_con_mas_duracion(fichero)[0]} con una duracion de {pelicula_con_mas_duracion(fichero)[1]} minutos")

def test_aux_dic(fichero):
    a = aux_dic(fichero)
    print(a)

def test_pelicula_con_mas_valoracion_por_anyo(fichero):
    a = pelicula_con_mas_valoracion_por_anyo(fichero)
    for k,v in a.items():
        print(f"{k} ----> {v}")
    #print(a)

def test_top_n_peliculas_por_genero(fichero):
    n = 2
    a = top_n_peliculas_por_genero(fichero, n)
    for k,v in a.items():
        print(f"{k} ----> {v}")

def test_tabla_generos(fichero):
    tabla_generos(fichero)

def test_dic_mes_sumvaloraciones(fichero):
    a = dic_mes_sumvaloraciones(fichero)
    for k,v in a.items():
        print(f"{k} ---- > {v}")
    #print(a)
if __name__ == "__main__":
    #test_lee_datos("Entrega 1\data\movie_dataset.csv")
    PELIS = lee_datos("Entrega 1\data\movie_dataset.csv")
    #test_filtra_por_categoria(PELIS)
    #test_calcular_media_duracion_por_categoria(PELIS)
    #test_top_pelicula_por_categoria_y_anyo(PELIS)
    #test_ordenar_por_rating_y_anyo(PELIS)
    #test_agrupar_por_categoria(PELIS)
    #test_contar_peliculas_por_anyo(PELIS)
    #test_pelicula_con_mas_duracion(PELIS)
    #test_aux_dic(PELIS)
    #test_pelicula_con_mas_valoracion_por_anyo(PELIS)
    #test_top_n_peliculas_por_genero(PELIS)
    #test_tabla_generos(PELIS)
    #test_dic_mes_sumvaloraciones(PELIS)