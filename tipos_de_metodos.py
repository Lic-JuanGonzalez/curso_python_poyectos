class Pajaro:

    alas = True

    # Contructor
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("El pajaro es de color {}".format(self.color))

    def volar(self, metros):
        print(f"El pajaro a volado {metros} metros")

    def pintar_negro(self):
        self.color = "negro"
        print(f"El pajaro ahora es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"El ave puso {cantidad} huevos")
        cls.alas = False
        print(cls.alas)

    @staticmethod
    def mirar():
        print("El pajaro mira")

# mi_pajaro = Pajaro("negro", "Tucan")

ave = Pajaro("amarillo", "canario")

# print(mi_pajaro.color)
# print(mi_pajaro.especie)

# print(f"mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")

# print(Pajaro.alas)
# print(mi_pajaro.alas)

ave.volar(50)
ave.piar()
ave.pintar_negro()
ave.poner_huevos(3)
Pajaro.mirar()



