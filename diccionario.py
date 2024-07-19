diccionario = {"c1":"valor1","c2":"valor2"}
print(type(diccionario))
print(diccionario)

resultado = diccionario["c1"]
print(resultado)


cliente = {
    "nombre":"Juan",
    "apellido":"Gonzalez",
    "peso":"71",
    "altura":"1.81"
}

consulta = (cliente["nombre"])
print(consulta)

diccionario2 = {"c1":55,"c2":[10,20,30],"c3":{"s1":100,"s2":200}}
print(diccionario2["c3"]["s2"])

diccionario3 = {"c1":["a","b","c"],"c2":["d","e","f"]}
print((diccionario3["c2"][1]).upper())

diccionario4 = {1:"a",2:"b"}
print(diccionario4)

diccionario4[3] = "c"
print(diccionario4)

diccionario4[2] = "B"
print(diccionario4)

print(diccionario4.keys())
print(diccionario4.values())
print(diccionario4.items())
