# palabra = "python"

# lista = []

# for letra in palabra:
#     lista.append(letra)

lista = [letra for letra in "python"]
print(lista)

lista2 = [n for n in range(0,21,2)]
print(lista2)

lista3 = [n/2 for n in range(0,21,2)]
print(lista3)

lista3 = [n if n*2 > 10 else "no" for n in range(0,21,2)]
print(lista3)

pies = [10,20,30,40,50]
metros = [round(p / 3.281,2) for p in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [v for v in valores if v % 2 == 0]
print(valores_pares)


