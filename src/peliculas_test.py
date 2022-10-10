


from peliculas import lee_datos
from peliculas2 import mostrar_numerado


if __name__ == "__main__":
    PELIS = lee_datos(".\data\movie_dataset.csv")
    print(PELIS)
    mostrar_numerado(PELIS)