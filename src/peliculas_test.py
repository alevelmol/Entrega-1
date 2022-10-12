


from peliculas import lee_datos
from peliculas2 import mostrar_numerado


def test_peliculas_leidas():
    PELIS = lee_datos(".\data\movie_dataset.csv")
    numerototal = len(PELIS)
    print(f"Se han leido {numerototal} películas")
    mostrar_numerado(PELIS)


if __name__ == "__main__":
    test_peliculas_leidas()