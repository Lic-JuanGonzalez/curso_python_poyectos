nombres = ["Ana","Hugo","Valeria"]
edades = [65,29,42]
cuidades = ["Lima","Madrid","Mexico"]

combinados = list(zip(nombres,edades,cuidades))

print(combinados)

for nombre,edad,cuidad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {cuidad}")


