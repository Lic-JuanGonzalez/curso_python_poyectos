import generadores

def eleccion_rubro():

    print("Bienvenido")

    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica")
        try:
            mi_rubro = input("Elija el area: ").upper()
            ["P", "F", "C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            break
    generadores.decorador(mi_rubro)

def inicio():

    while True:
        eleccion_rubro()
        try:
            otro_turno = input("Quieres ssacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            if otro_turno == "N":
                print("gracias por su visita")
                break

inicio()
