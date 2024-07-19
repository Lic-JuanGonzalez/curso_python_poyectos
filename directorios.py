import os
from pathlib import Path, PureWindowsPath

# ruta = os.getcwdb()
# ruta = os.chdir("C:\\Users\\User\\Desktop\\Cursos\\2.Python\\tratamiento_by_os\\prueba.txt")
# ruta = os.makedirs("C:\\Users\\User\\Desktop\\Cursos\\2.Python\\tratamiento_by_os\\nuevo_directorio")
# ruta = "C:\\Users\\User\\Desktop\\Cursos\\2.Python\\tratamiento_by_os\\prueba.txt"

# print(ruta)

# elemento = os.path.basename(ruta)
# print(elemento)

# elemento = os.path.dirname(ruta)
# print(elemento)

# elemento = os.path.split(ruta)
# print(elemento)

# ruta = os.rmdir("C:\\Users\\User\\Desktop\\Cursos\\2.Python\\tratamiento_by_os\\nuevo_directorio")

# archivo = open("prueba.txt")
# print(archivo.read())

# otra_ruta = open("C:\\Users\\User\\Desktop\\Cursos\\2.Python\\tratamiento_by_os\\prueba.txt")
# print(otra_ruta.read())

# Para usuarios de otros sistemas operativos

# carpeta = Path('C:/Users/User/Desktop/Cursos/2.Python/tratamiento_by_os')
# archivo = carpeta / "prueba.txt"

# mi_archivo = open(archivo)
# print(mi_archivo.read())

# carpeta = Path('C:/Users/User/Desktop/Cursos/2.Python/tratamiento_by_os') / "prueba.txt"
# mi_archivo = open(carpeta)
# print(mi_archivo.read())

carpeta = Path('C:/Users/User/Desktop/Cursos/2.Python/tratamiento_by_os/prueba.txt')

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)

# print(carpeta.read_text())
# print(carpeta.name)
# print(carpeta.suffix)
# print(carpeta.stem)

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Este archivo existe")




