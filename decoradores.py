"""

@classmethod
@staticmethod

Tambien son decoradores pero la
idea principal es que funcionen
como un Swiich

"""

"""
Primera Opcion
def mayuscula_saludo(texto):
    print("Hola!")
    print(texto.upper())
    print("Adios!")

def mayuscula(texto):
    print(texto.upper())
"""
"""
Segunda Opcion

print("Hola!")
mayuscula("Hoy es lunes")
print("Adios!")
"""

"""def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    def una_funcion(funcion):
        return funcion

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula

operacion = cambiar_letras("may")
operacion("palabra")
"""
"""
Alternativa no es optima

mi_funcion = mayuscula
mi_funcion("python")

La funcion como tal se pasa como argumento de otra funcion
una_funcion(mayuscula("probando"))

"""

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otra_funcion

"""
Opcion recomendada pero no opctima

@decorar_saludo
def mayuscula(texto):
    print(texto.upper())
@decorar_saludo
def minuscula(texto):
    print(texto.lower())

mayuscula("python")
minuscula("PYTHON")
"""
# Opcion recomendada

def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

mayuscula_decorada = decorar_saludo(mayuscula)

mayuscula("python")
mayuscula_decorada("python")
