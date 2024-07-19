from collections import Counter
from collections import defaultdict
from collections import namedtuple

numeros = [8,2,3,4,5,5,2,3,2,21,100]
print(Counter(numeros))

print(Counter("mississippi"))

frase = "al pan pan y al vino vino"
print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,4])

print(serie.most_common())
print(list(serie))

mi_dic = {"uno":"verde", "dos":"azul", "tres":"rojo"}
print(mi_dic["dos"])

mi_dic2 = defaultdict(lambda: "none")

mi_dic2["uno"] = "verde"

print(mi_dic2["dos"])

print(mi_dic2)

mi_tupla = (500, 18, 65)
print(mi_tupla[1])

Persona = namedtuple("persona", ['nombre', 'altura', 'peso'])
juan = Persona("Juan", "1.80", "70")

print(juan.altura)
print(juan.peso)

print(juan[2])


