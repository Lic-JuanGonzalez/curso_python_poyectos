# class Animal:
#
#     def __init__(self, edad, color):
#         self.edad = edad
#         self.color = color
#     def nacer(self):
#         print("Este animal a nacido")
#
#     def hablar(self):
#         print("Este animal emite un sonido")
# class Pajaro(Animal):
#
#     def __init__(self, edad, color, altura_vuela):
#         super().__init__(edad,color)
#         # Se reemplaza como en java en el constructor
#         # self.edad = edad
#         # self.color = color
#         self.altura_vuelo = altura_vuela
#     def hablar(self):
#         print("Este pajaro puede copiar frases")
#
#     def volar(self, metros):
#         print(f"El pajaro vuela {metros} metros")
#
#
# # print(Pajaro.__bases__)
# # print(Animal.__subclasses__())
#
# mi_animal = Animal(5, "Negro")
#
# mi_pajaro = Pajaro(2, "amarillo")
#
# print(mi_pajaro.edad)
# print(mi_pajaro.color)
#
# mi_pajaro.nacer()
# mi_pajaro.hablar()
# mi_pajaro.volar(10)

class Padre:
    def hablar(self):
        print("Hola!!")

class Madre:
    def reir(self):
        print("Jajaja!")

    def hablar(self):
        print("Que tal!")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar()
mi_nieto.reir()

# Orden de resolucion de metodos(orden de prioridad)
print(Nieto.__mro__)
