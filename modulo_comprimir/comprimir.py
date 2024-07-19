import zipfile
import shutil

# mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "w")

# mi_zip.write("mi_texto_A.txt")
# mi_zip.write("mi_texto_B.txt")

# mi_zip.close()

# zip_abierto = zipfile.ZipFile("archivo_comprimido.zip", "r")

# zip_abierto.extractall()


# carpeta_origen = "C:\\Users\\juann\Desktop\\Cursos\\2.Python\modulo_comprimir\\Europa"

# archivo_destino = "Europa_comprimido"

# shutil.make_archive(archivo_destino, "zip", carpeta_origen)

shutil.unpack_archive("Europa_comprimido.zip", "Europa Extraccion Terminada", "zip")

