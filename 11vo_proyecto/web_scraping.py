import bs4
import requests

# Crear url son numero de pagina
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

# Lista de titulos con 4-5 estrellas

titulos_rating_buscado = []

# Iterar pagina
for pagina in range(1, 51):

    # Crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    # Seleccionar datos de los libros
    libros = sopa.select(".product_pod")

    # Iterar libros
    for libro in libros:

        # Verificar que tengan 4-5 estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:

            # Guardar titulo en variable
            titulo_libro = libro.select("a")[1]["title"]

            # Agregar libro a la lista
            titulos_rating_buscado.append(titulo_libro)

# Mostrar los libros selccionados
for t in titulos_rating_buscado:
    print(t)
