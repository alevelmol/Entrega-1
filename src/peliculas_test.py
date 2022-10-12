


from peliculas import lee_datos
from peliculas2 import mostrar_numerado
PELIS = lee_datos(".\data\movie_dataset.csv")


def test_peliculas_leidas():
    numerototal = len(PELIS)
    print(f"Se han leido {numerototal} películas")
    mostrar_numerado(PELIS)


def test_tres_primeras_pelis():
    print("Mostrando en pantalla las tres primeras películas:")
    mostrar_numerado(PELIS[:3])


def test_tres_ultimas_pelis():
    print("Mostrando en pantalla las tres últimas películas:")
    mostrar_numerado(PELIS[-3:])


if __name__ == "__main__":
    #test_peliculas_leidas()
    #test_tres_primeras_pelis()
    #test_tres_ultimas_pelis()