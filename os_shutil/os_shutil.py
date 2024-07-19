import os
import shutil
import send2trash

# print(os.getcwd())

# archivo = open("curso.txt", "w")
# archivo.write('texto de prueba')
# archivo.close()

# print(os.listdir())

# shutil.move("curso.txt", "os_shutil/")

# os.unlink() arhicvo
# os.rmdir() carpeta vacia

# shutil.rmtree() elimina todo sin preguntar

# send2trash.send2trash("curso.txt")

# print(os.walk("C:\\Users\\juann\\Desktop\\Cursos\\2.Python\\Europa"))

ruta = "C:\\Users\\juann\\Desktop\\Cursos\\2.Python\\Europa"

for carpeta, sub_carpeta, archivo in os.walk(ruta):
    print(f"En la carpeta {carpeta}")
    print(f"Las subcarpetas son {sub_carpeta}")
    for sub in sub_carpeta:
        print(f"\t{sub}")
    print(f"Los archivos son: ")
    for arch in archivo:
        # if arch.startswith("2015"):
        #     print(f"\t{arch}")
        print(f"\t{arch}")
    print("\t")
