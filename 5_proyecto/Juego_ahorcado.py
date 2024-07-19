import random
from random import *

print("///////////////////////////")
print("////Juego del Ahoracado////")
print("///////////////////////////")

aciertos = 0
vidas = 6
palabras = ("auto","naranja","elefante","casa")
letras_correctas = []
letras_incorrectas = []
juego_terminado = False


def palabra_elegida(palabras):
    palabra_elegida = choice(palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida,letras_unicas

def pedir_letra():

    letra_elegida = ""
    es_valida = False
    abc = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ").lower()
        if letra_elegida in abc and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido un caracter correcto")

    return letra_elegida

def mostrar_nuevo_tablero(palaabra_elegida):

    lista_oculta = []

    for letra in palaabra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append("-")

    print(f" ".join(lista_oculta))

def estado_letra(letra_elegida, palabra_oculta, vidas, coincidencias):

    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("La letra elegida, ya ha sido encontrada")
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias

def perder():
    print("Te has quedado sin vidas")
    print(f"La palabra era {palabra}")

    return True

def ganar(palabra_oculta):
    mostrar_nuevo_tablero(palabra_oculta)
    print(f"Has ganado")
    print(f"La palabra era {palabra}")

    return True

palabra, letras_unicas = palabra_elegida(palabras)

while not juego_terminado:
    print("\n" + "*" * 20 + "\n")
    mostrar_nuevo_tablero(palabra)
    print("\n")
    print("Letras incorrectas: " + "-".join(letras_incorrectas))
    print(f"Vidas: {vidas}")
    print("\n" + "*" * 20 + "\n")
    letra = pedir_letra()

    vidas, terminado, aciertos = estado_letra(letra, palabra, vidas, aciertos)

    juego_terminado = terminado
