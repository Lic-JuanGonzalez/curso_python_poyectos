from random import *

intentos = 1

while True:
  random = randint(1, 100)
  print("|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-|")
  print("| A D I V I N A  E L  N U M E R O |")
  print("|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-|\n")

  print("1: Empezar a jugar")
  print("0: Salir")
  print("Elige una opcion: ")

  opcion = int(input())
  print("\n")

  if opcion == 1:
      intentos = 1

  elif opcion == 0:
      print("¡Gracias por jugar!")
      break

  else:
      print("Opcion invalida. Intenta de nuevo.")

  while intentos < 8:
    print("Intento numero: " + str(intentos))
    numero = int(input("Numero: "))
    intentos += 1

    if(numero > 100 or numero < 0):
        print("El numero esta comprendido entre 0 y 100")

    else:
        if (numero > random):
            print("El numero es menor al escrito")
        if (numero < random):
            print("El numero es mayor al escrito")
        if (numero == random):
            print(f"GANASTE, Has acertado al numero que era {random}, en {intentos-1} intentos")
            break
        else:
            print("Has perdido")
