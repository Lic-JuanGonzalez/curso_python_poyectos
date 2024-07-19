print("//////////////////////////////")
print("---- ANALIZADOR DE TEXTO -----")
print("//////////////////////////////")

texto = input("Ingresa el texto a analizar: ")
texto = texto.lower()

letras = []
letras.append(input("Ingresa la primera letra a analizar: ").lower())
letras.append(input("Ingresa la segunda letra a analizar: ").lower())
letras.append(input("Ingresa la tercera letra a analizar: ").lower())

print("\n")

cant_letras1 = texto.count(letras[0])
cant_letras2 = texto.count(letras[1])
cant_letras3 = texto.count(letras[2])

print("|----------------------|")
print("|- CANTIDAD DE LETRAS -|")
print("|----------------------|")

print(f"La letra {letras[0]} se encuentra en el texto {cant_letras1} veces")
print(f"La letra {letras[1]} se encuentra en el texto {cant_letras2} veces")
print(f"La letra {letras[2]} se encuentra en el texto {cant_letras3} veces")

print("\n")

print("|------------------------|")
print("|- CANTIDAD DE PALABRAS -|")
print("|------------------------|")

palabras = texto.split()
print(f"El texto posee {len(palabras)} palabras")

print("\n")

print("|--------------------------|")
print("|- LETRAS DE INICIO Y FIN -|")
print("|--------------------------|")

print(f"El texto inicia con la palabra '{palabras[0]}' y finaliza con la palabra '{palabras[-1]}'")

print("\n")

print("|-------------------|")
print("|- TEXTO INVERTIDO -|")
print("|-------------------|")

palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"El texto si lo invertimos queda de la siguiente manera: '{texto_invertido}'")

print("\n")

print("|-------------------|")
print("|- PALABRA PYTHON -|")
print("|-------------------|")

python = "python" in texto

dic = {True:"SI", False:"NO"}
print(f"La palabra 'Python' {dic[python]} aparece en el texto")

# if (python == True):
#     print("La palabra 'python' SI aparece en el texto")
# else:
#     print("La palabra 'python' NO aparece en el texto")
