def devolver_distintos(n1, n2, n3):

    suma = n1 + n2 + n3

    if (suma > 15):
        return max(n1, n2, n3)
    elif (suma < 10):
        return min(n1, n2, n3)
    elif (10 <= suma <= 15):
        num_ord = sorted([n1,n2,n3])

        return num_ord[1]



resultado = devolver_distintos(4,5,3)
print(resultado)


def analizador_palabra(palabra):

    palabra_ord = set(palabra)
    palabra_ord = sorted(palabra_ord)

    return palabra_ord


pal1 =analizador_palabra("entretenido")
print(pal1)

def analizador_ceros(*args):

    lista_numeros = list(args)

    for i in range(len(lista_numeros) - 1):

        if lista_numeros[i] == 0 and lista_numeros[i + 1] == 0:
            return True

    return False


resultado = analizador_ceros(5,6,1,0,0,9,3,5)
print(resultado)

def contar_primos(numero):

    contador_primos = [2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:

        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            contador_primos.append(iteracion)
            iteracion += 2

    print(contador_primos)
    return len(contador_primos)

print(contar_primos(100))
