lista = ['a','b','c']

for l in lista:
    numero_letra = lista.index(l) + 1
    print(f"Letra {numero_letra}: {l}")

lista2 = ["pablo", "laura", "fede", "luis", "julia"]

for nombre in lista2:
    if nombre.startswith("l"):
        print(nombre)

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

# palabra = "python es genial"
# for letra in palabra:
#     print(letra)

for letra in "python":
    print(letra)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

dic = {"clave1":"a","clave2":"b","clave3":"c"}
for a,b in dic.items():
    print(a,b)
