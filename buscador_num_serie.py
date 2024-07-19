import re, os, time, datetime
from pathlib import Path
import math

ruta = "C:\\Users\\juann\\Desktop\\Cursos\\2.Python\\9no proyecto\\data\\Mi_Gran_Directorio"
mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
numeros_emcontrados = []
archivos_encontrados = []
inicio = time.time()


def buscar_numero(archivo, patron):

    este_archivo = open(archivo, "r")
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ""

def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a), mi_patron)
            if resultado != '':
                numeros_emcontrados.append(resultado.group())
                archivos_encontrados.append(a.title())

def mostrar_informacion():

    indice = 0

    print("-" * 50)
    print(f"Fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}")
    print("\n")
    print("A R C H I V O\t\t\tNRO. SERIE")
    print("-------------\t\t\t----------")

    for a in archivos_encontrados:
        print(f"{a}\t{numeros_emcontrados[indice]}")
        indice += 1

    print('\n')
    print(f"Numeros encontrados: {len(numeros_emcontrados)}")

    fin = time.time()
    duracion = fin - inicio
    print(f"Duracion de la busqueda: {math.ceil(duracion)} segundos")
    print("-" * 50)

crear_listas()
mostrar_informacion()
