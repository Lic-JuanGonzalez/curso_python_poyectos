import bs4
import requests

resultado = requests.get("https://es.wikipedia.org/wiki/Argentina")

# print(type(resultado))
#print(resultado.text) #HTML completo

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

# parrafo_especial = sopa.select("title")[0].getText()
# print(parrafo_especial.getText())

# tarjeta = sopa.select(".three-elements-chain-item .story-card-ctn a")
#
# for p in tarjeta:
#     print(p.getText())

imagenes = sopa.select(".mw-file-description img")[0]
url = imagenes.get("src")
if url.startswith("//"):
    url = "https:" + url
print(url)

imagen_1 = requests.get(url)
# print(imagen_1.content)

f = open('mi_imagen.jpg', "wb")
f.write(imagen_1.content)
f.close()
