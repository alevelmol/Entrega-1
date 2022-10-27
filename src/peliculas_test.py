


from peliculas import *
from peliculas2 import mostrar_numerado
PELIS = lee_datos("./data/movie_dataset.csv")


def test_peliculas_leidas():
    peliculas_leidas(PELIS)
def test_tres_primeras_pelis():
    tres_primeras_pelis(PELIS)
def test_tres_ultimas_pelis():
    tres_ultimas_pelis(PELIS)
def test_filtra_por_categoria():
    categoria = "Comedy"
    print(f"Las películas con la categoria {categoria} son:")
    mostrar_numerado(filtra_por_categoria(PELIS, categoria))
def test_calcular_media_duracion_por_categoria():
    categoria = "Comedy"
    print(f"La media de las duraciones de las películas de la categoría {categoria} es: ")
    print(calcular_media_duracion_por_categoria(PELIS, categoria))

if __name__ == "__main__":
    #test_peliculas_leidas()
    #test_tres_primeras_pelis()
    #test_tres_ultimas_pelis()
    #test_filtra_por_categoria()
    test_calcular_media_duracion_por_categoria()