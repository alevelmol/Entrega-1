


from peliculas import *
from peliculas2 import mostrar_numerado
PELIS = lee_datos(".\data\movie_dataset.csv")


def test_peliculas_leidas():
    peliculas_leidas(PELIS)


def test_tres_primeras_pelis():
    tres_primeras_pelis(PELIS)


def test_tres_ultimas_pelis():
    tres_ultimas_pelis(PELIS)


if __name__ == "__main__":
    #test_peliculas_leidas()
    #test_tres_primeras_pelis()
    #test_tres_ultimas_pelis()