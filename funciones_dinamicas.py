def chequear_3_cifras(lista):

    lista_3 = []

    for n in lista:
        if n in range(100,1000):
            lista_3.append(n)
        else:
            pass
    return lista_3

resultado = chequear_3_cifras([555,99,600])
print(resultado)


