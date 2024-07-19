import os
from pathlib import Path

mi_ruta = Path("Recetas")
finalizar = False

def cant_recetas(ruta):
    cant_recetas = 0
    for txt in Path(ruta).glob("**/*.txt"):
        cant_recetas += 1
    return cant_recetas

def inicio():
    os.system("cls" if os.name == "nt" else "clear")
    print("/" * 27)
    print("//// R E C E T A R I O ////")
    print("/" * 27 + "\n")
    print(f'Las recetas se encuentran en "{mi_ruta}"')
    print(f"Total de recetas: {cant_recetas(mi_ruta)}")

    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        print("Elige una opción: ")
        print("""
        [1] Leer receta
        [2] Crear receta
        [3] Crear categoría
        [4] Eliminar receta
        [5] Eliminar categoría
        [6] Finalizar""")
        eleccion_menu = input()

    return int(eleccion_menu)

def mostrar_categorias(ruta):
    print("Categorías")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    cant = 0

    for carpeta in ruta_categorias.iterdir():
        if carpeta.is_dir():
            carpeta_str = carpeta.name
            print(f"[{cant + 1}] - {carpeta_str}")
            lista_categorias.append(carpeta)
            cant += 1

    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = "x"
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElige una categoría: ")

    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("Recetas")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    cant = 0

    for receta in ruta_recetas.glob("*.txt"):
        receta_str = receta.name
        print(f"[{cant + 1}] - {receta_str}")
        lista_recetas.append(receta)
        cant += 1

    return lista_recetas

def elegir_receta(lista):
    eleccion_receta = "x"
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElige una receta: ")

    return lista[int(eleccion_receta) - 1]

def leer_receta(receta):
    print("\nContenido de la receta:\n")
    print(Path(receta).read_text())

def crear_receta(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + ".txt"
        print("Escribe la receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not ruta_nueva.exists():
            ruta_nueva.write_text(contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido CREADA")
            existe = True
        else:
            print("ERROR... La receta ya existe")

def crear_categoria(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de tu categoría: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not ruta_nueva.exists():
            ruta_nueva.mkdir()
            print(f"Tu categoría {nombre_categoria} ha sido CREADA")
            existe = True
        else:
            print("ERROR... La categoría ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido ELIMINADA")

def eliminar_categoria(categoria):
    try:
        Path(categoria).rmdir()
        print(f"La categoría {categoria.name} ha sido ELIMINADA")
    except OSError:
        print("ERROR... La categoría no está vacía o no se puede eliminar")

def volver_inicio():
    eleccion_regresar = ""
    while eleccion_regresar.lower() != "v":
        eleccion_regresar = input("\nPresiona 'v' para volver al menú: ")

while not finalizar:
    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        if mis_categorias:
            mi_categoria = elegir_categoria(mis_categorias)
            mis_recetas = mostrar_recetas(mi_categoria)
            if mis_recetas:
                mi_receta = elegir_receta(mis_recetas)
                leer_receta(mi_receta)
            else:
                print("No hay recetas en esta categoría.")
        else:
            print("No hay categorías disponibles.")
        volver_inicio()
    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        if mis_categorias:
            mi_categoria = elegir_categoria(mis_categorias)
            crear_receta(mi_categoria)
        else:
            print("No hay categorías disponibles.")
        volver_inicio()
    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()
    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        if mis_categorias:
            mi_categoria = elegir_categoria(mis_categorias)
            mis_recetas = mostrar_recetas(mi_categoria)
            if mis_recetas:
                mi_receta = elegir_receta(mis_recetas)
                eliminar_receta(mi_receta)
            else:
                print("No hay recetas en esta categoría.")
        else:
            print("No hay categorías disponibles.")
        volver_inicio()
    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        if mis_categorias:
            mi_categoria = elegir_categoria(mis_categorias)
            eliminar_categoria(mi_categoria)
        else:
            print("No hay categorías disponibles.")
        volver_inicio()
    elif menu == 6:
        print("Programa Finalizado")
        finalizar = True
