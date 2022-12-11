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

`Pelis = namedtuple("Pelis", "day, month, year, fecha, duration, title, subject, actor, actress, director, popularity, awards, rate")`

en la que cada variable es de tipo:

`Pelis = namedtuple("Pelis", "str, str, str, datetime, int, str, str, str, str, str, int, boolean, float")`

## Funciones implementadas
En este proyecto se han implementado las siguientes funciones, divididas en cada uno de los módulos en los que se encuentran.

### Módulo peliculas
Es el módulo principal, en el que se encuentran definidas las funciones del proyecto, para posteriormente probarlas en el módulo peliculas_test
#### Entrega 1
  * **lee_datos(fichero)**: Función que lee el database y guarda los datos en una lista de tuplas de tipo Pelis. Para implementar la función se ha recurrido a una serie de funciones auxiliares localizadas en el [modulo `peliculas2`]
    * **parse_bool**: Función para convertir cadena de texto en booleano
    * **parse_float**: Función para convertir cadena de texto en float
    * **parse_int**: Función para convertir cadena de texto en int
    * **mostrar_enumerado**: Función que enumera e imprime una lista de tuplas de manera ordenada

#### Entrega 2
  * **Bloque 1**
    * **filtra_por_categoria(fichero, categoria)**: Función que, dados un fichero y una categoria, devuelve las listas de tuplas, correspondientes a todas las películas de la categoria introducida
    * **calcular_media_duracion_por_categoria(fichero, categoria)**: Funcion que, dados un fichero y una categoria, devuelve un valor float, correspondiente a la media de las duraciones de las películas de la categoría indicada.
  * **Bloque 2**
    * **top_pelicula_por_categoria_y_anyo(fichero, anyo, categoria="Comedy")**: Función que, dados un fichero, un año y una categoria(la cual tiene como valor predeterminado "Comedy"), devuelve a tupla correspondiente a la mejor pelicula del año y categoria indicados
    * **ordenar_por_rating_y_anyo(fichero, anyo)**: Función que, dados un fichero y un año, devuelve una lista de tuplas, con el titulo y la valoración de la pelicula, ordenadas de mayor a menor valoracion, del año introducido en la funcion.
    * **agrupar_por_categoria(fichero)**: Función que, dado un fichero, devuelve un diccionario cuyas claves son las diferentes categorias de las peliculas, y los valores, aquellas películas que tengan dicha categoria

#### Entrega 3
  * **Bloque 3**
    * **contar_peliculas_por_anyo(fichero)**: Funcion que, dado un fichero, devuelve un diccionario cuyas claves son los años y los valores, las peliculas estrenadas en dicho año.
    * **pelicula_con_mas_duracion(fichero)**: Funcion que, dado un fichero, devuelve una tupla conformada por el titulo de la pelicula y su duracion, en minutos.
    * **aux_dic(fichero)**: Funcion auxiliar que, dado un fichero, devuelve una lista de tuplas conformadas por una tupla con titulo y año, y la valoracion de la pelicula.
    * **pelicula_con_mas_valoracion_por_anyo(fichero)**: Funcion que, dado un fichero y empleando una funcion auxiliar, devuelve un diccionario cuyas claves son los años y los valores son el titulo de la pelicula y su correspondiente valoracion.
    * **aux_dic_2(fichero)**: Funcion auxiliar que, dado un fichero, devuelve una lista de tuplas conformadas por una tupla con titulo y genero, y la valoracion de la pelicula
    * **top_n_peliculas_por_genero(fichero, n=3)**: Funcion que, dado un fichero y empleando una funcion auxiliar, devuelve un diccionario cuyas claves son los generos y los valores son el titulo de la pelicula y su correspondiente valoracion.
  * **Bloque 4**
    * **tabla_generos(fichero)**: Funcion que, dado un fichero, devuelve un grafico cuyo eje x son los generos y cuyo eje y son las peliculas con dicho genero
### Módulo peliculas_test
En el módulo de pruebas se han definido las funciones para probar el funcionamiento de las funciones del módulo películas. Es decir, cada función definida en el módulo peliculas tiene su correspondiente función para probar su funcionamiento. Por ejemplo, la funcion `test_lee_datos` ejecuta la función `lee_datos`, definida en el módulo principal. Dentro del test de lee_datos, se haya contenido las pruebas pertinentes (mostrar los datos leidos, mostrar las tres primeras y las tres ultimas peliculas del dataset)
* **test_lee_datos**:
* **test_filtra_por_categoria**
* **test_calcular_media_duracion_por_categoria**
* **test_top_pelicula_por_categoria_y_anyo**
* **test_ordenar_por_rating_y_anyo**
* **test_agrupar_por_categoria**
* **test_contar_peliculas_por_anyo**
* **test_pelicula_con_mas_duracion**
* **test_pelicula_con_mas_valoracion_por_anyo**
* **test_top_n_peliculas_por_genero**
* **test_tabla_generos**

### Módulo peliculas2
En este módulo se hayan las funciones de parseo, más la función de mostrar_enumerado
* **parse_bool**: Función para convertir cadena de texto en booleano. Si la cadena recibida es un Yes, devuelve el valor True, y si la cadena recibida es un No, devuelve el valor False
* **parse_float**: Función para convertir cadena de texto en float
* **parse_int**: Función para convertir cadena de texto en integer
* **mostrar_enumerado**: Función que enumera e imprime una lista de tuplas de manera ordenada.
