import re

"""
texto = "Me llamo Juan Gonzalez y soy Licenciado en informatica y desarrollo de software y em recibi el 29-02-2024 de 2024"

palabra = 'recibi' in texto
print(palabra)

patron = 'Lucas'
patron2 = 'Juan'
patron3 = 'de'
busqueda = re.search(patron2, texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())

busqueda2 = re.findall(patron3, texto)
print(busqueda2)
print(len(busqueda2))

for match in re.finditer(patron3, texto):
    print(match.span())

"""

"""
texto = "llama al 564-525-6588 ya mismo"
# patron = r'\d\d\d-\d\d\d-\d\d\d\d'
# patron = r'\d{3}-\d{3}-\d{4}'
patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

resultado = re.search(patron, texto)
print(resultado)
print(resultado.group())
print(resultado.group(2))
"""
"""
clave = input("clave: ")

patron = r'\D{1}\w{7}'
chequear = re.search(patron, clave)

print(chequear)
"""

texto = "No atendemos los lunes por la tarde"

# buscar = re.search(r'lunes|martes', texto)
# buscar = re.search(r'....demos...', texto)
# buscar = re.search(r'^\D', texto)
# buscar = re.search(r'\D$', texto)
# buscar = re.findall(r'[^\s]', texto)
buscar = re.findall(r'[^\s]+', texto)

# print(buscar)
print("".join(buscar))
