# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  22/23)
Autor/a: Alejandro Vela Molina   uvus: alevelmol

El proyecto entregado tiene como objetivo leer y analizar datos acerca de algunas de las películas más importantes de la historia, dichos datos se pueden encontrar en el siguiente enlace (http://kaggle.com/paramarthasengupta/top-movies-database-19202000s). El dataset original poseía algunas fechas incorrectas (31/04, 29/02, ...), las cuales han sido corregidas a mano. La columna rate, por su parte, poseía los datos tipo float con comas en vez de con puntos. Dicha sustitución se haya en el código. Se ha creado tambíen una nueva variable en el namedtuple, la cual unifica las variables day, month y year, para poder emplear el formato datatime.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<peliculas.py\>**: Contiene las funciones para tratar el dataset
  * **\<peliculas_test.py\>**: Contiene las funciones para testear el funcionamiento del módulo `peliculas.py`. En este módulo aparece el main
  * **\<peliculas2.py\>**: Contiene las funciones de parseo de booleano y el enumerado para imprimir las películas
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<movie_dataset.csv\>**: Contiene la lista de las películas, para cada película se dan datos como la fecha de lanzamiento, director, actores, popularidad, si ganaron o no premio, etc..
    
## Estructura del *dataset*

Cada fila del dataset contiene los datos de las películas más famosas de los años 1990-2000. Aparte de las 12 columnas, se ha añadido una variable más, que no corresponde a ninguna columna, llamada fecha, la cual junta las variables day, month, year, en formate datetime

El dataset está compuesto por 12 columnas, con la siguiente descripción:

* **day**: de tipo str, representa el día de salida de la película
* **month**: de tipo str, representa el mes de salida de la película
* **year**: de tipo str, representa el año de salida de la película.
* **duration** de tipo int, representa la duración de la película, en minutos.
* **title** de tipo str, representa el título de la película
* **subject** de tipo str, representa el género de la película
* **actor** de tipo str, representa el actor principal de la película
* **actress** de tipo str, representa la actriz principal de la película
* **director** de tipo str, representa el director de la película
* **popularity** de tipo int, representa la popularidad de la película
* **awards** de tipo bool, representa si la película ha sido premiada o no
* **rate** de tipo float, representa la puntuación recibida de la película
* **fecha** de tipo datetime, representa la fecha exacta del lanzamiento.

## Tipos implementados

Para trabajar con los datos del dataset se ha definido la siguiente tupla con nombre:

`pelis = namedtuple("Lista", "day, month, year, fecha, duration, title, subject, actor, actress, director, popularity, awards, rate")`

en la que cada variable es de tipo:

`pelis = namedtuple("Lista", "str, str, str, datetime, int, str, str, str, str, str, int, boolean, float")`

## Funciones implementadas
En este proyecto se han implementado las siguientes funciones, divididas en cada uno de los módulos en los que se encuentran.

### Módulo peliculas
Es el módulo principal, en el que se encuentran definidas las funciones del proyecto, para posteriormente probarlas en el módulo peliculas_test
* **lee_datos(fichero)**: Función que lee el database y guarda los datos en una lista de tuplas de tipo Lista. Para implementar la función se ha recurrido a una serie de funciones auxiliares localizadas en el [modulo `peliculas2`]
  * **parse_bool**: Función para convertir cadena de texto en booleano
  * **parse_float**: Función para convertir cadena de texto en float
  * **parse_int**: Función para convertir cadena de texto en int
* **peliculas_leidas(fichero)**: Función que, a partir del fichero, lee cuantas películas hay y las imprime todas, enumeradas, apoyándose en la función `mostrar_enumerado`
  * **mostrar_enumerado**: Función que enumera e imprime una lista de tuplas de manera ordenada
* **tres_primeras_peliculas(fichero)**: Función que muestra en pantalla las tres primeras películas del dataset. Se apoya también en la función `mostrar_enumerado`
* **tres_ultimas_peliculas(fichero)**: Función que muestra en pantalla las tres últimas películas del dataset. Se apoya también en la función `mostrar_enumerado`

### Módulo peliculas_test
En el módulo de pruebas se han definido las funciones para probar el funcionamiento de las funciones del módulo películas. Es decir, cada función definida en el módulo peliculas tiene su correspondiente función para probar su funcionamiento. Por ejemplo, la funcion `test_peliculas_leidas` ejecuta la función `peliculas_leidas`, definida en el módulo principal
* **test_peliculas_leidas()**:
* **test_tres_primeras_peliculas()**:
* **test_tres_ultimas_peliculas()**:
### Módulo peliculas2
En este módulo se hayan las funciones de parseo, más la función de mostrar_enumerado
* **parse_bool**: Función para convertir cadena de texto en booleano. Si la cadena recibida es un Yes, devuelve el valor True, y si la cadena recibida es un No, devuelve el valor False
* **parse_float**: Función para convertir cadena de texto en float
* **parse_int**: Función para convertir cadena de texto en integer
* **mostrar_enumerado**: Función que enumera e imprime una lista de tuplas de manera ordenada.
