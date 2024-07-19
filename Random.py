from random import *

aleatorio1 = randint(1,50)
print(aleatorio1)

aleatorio2 = round(uniform(1,5),1)
print(aleatorio2)

aleatorio3 = random()
print(aleatorio3)

colores = ["azul","rojo","verde","amarillo"]
aleatorio4 = choice(colores)
print(aleatorio4)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)


