def parse_bool(cadena):
    if cadena == "Yes":
        booleano = True
    else:
        booleano = False
    return booleano

def mostrar_numerado(coleccion):
    i=0
    for p in coleccion:
        i=i+1
        print (i, p) 

def parse_int(cadena):
    return int(cadena)

def parse_float(cadena):
    return float(cadena)