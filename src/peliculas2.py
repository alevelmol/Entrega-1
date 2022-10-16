def parse_bool(cadena):
    '''
    A partir de una cadena, si la cadena contiene el valor Yes, la función devuelve el lógico True, y si la cadena contiene el valor No, la función devuelve el lógico False
    Parametro: Cadena con los valores "Yes" or "No".
    Formato: Cadena: str
    Devuelve: True o False, dependiendo del valor de la cadena.
    Formato del resultado: bool
    '''
    if cadena == "Yes":
        booleano = True
    else:
        booleano = False
    return booleano

def mostrar_numerado(coleccion):
    '''
    A partir de una colección de datos, devuelve esa colección de datos, pero enumerada desde 1 hasta el último valor de la colección(última fila)
    Parametro: Colección con listas de tuplas
    Formato: Coleccion: Lista
    Devuelve: Enumeración de las listas de tupla
    '''
    i=0
    for p in coleccion:
        i=i+1
        print (i, p) 

def parse_int(cadena):
    '''
    A partir de una cadena de texto, devuelve la cadena, convertida a entero.
    Parametro: Número en formato str
    Formato: Cadena: str
    Devuelve: El número, en formato entero
    Formato del resultado: int
    '''
    return int(cadena)

def parse_float(cadena):
    '''
    A partir de una cadena de texto, devuelve la cadena, convertida a decimal.
    Parametro: Número en formato str
    Formato: Cadena: str
    Devuelve: El número, en formato decimal
    Formato del resultado: float
    '''
    return float(cadena)