"""def suma():
    ni = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(ni + n2)
    print("gracias por sumar!")

try:
    suma()
except TypeError:
    print("Estas intentado concatenar tipos distintos")
except ValueError:
    print("Ese no es un numero")
else:
    print("Se ejecuto correctamente")
finally:
    print("Final de codigo")"""

def pedir_numero():

    while True:
        try:
            numero = int(input("Numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias!")

pedir_numero()

