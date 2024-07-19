import time
import timeit
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

inicio = time.time()
prueba_for(100000)
final = time.time()
print(final - inicio)

inicio = time.time()
prueba_while(100000)
final = time.time()
print(final - inicio)

declaracion_for = """
prueba_for(10) # cuantas veces se repite el mismo codigo
"""

mi_setup_for = """
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
"""

declaracion_while = """
prueba_while(10) # cuantas veces se repite el mismo codigo
"""

mi_setup_while = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
"""

duracion_for = timeit.timeit(declaracion_for, mi_setup_for, number=1000000)
print(duracion_for)

duracion_while = timeit.timeit(declaracion_while, mi_setup_while, number=1000000)
print(duracion_while)
