mi_archivo = (open("prueba.txt"))
# print(mi_archivo)

# texto = mi_archivo.read()
# print(texto)

# primer_linea = mi_archivo.readline()
# print(primer_linea.upper())
#
# primer_linea = mi_archivo.readline()
# print(primer_linea.rstrip())
#
# primer_linea = mi_archivo.readline()
# print(primer_linea)

# for l in mi_archivo:
#     print(f"Aqui dice: {l}")

todas = mi_archivo.readlines()
print(todas)

todas = todas.pop()

mi_archivo.close()


