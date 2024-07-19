def num_perfumeria():
    for n in range(1,1000):
        yield f"P - {n}"

def num_farmacia():
    for n in range(1,1000):
        yield f"F - {n}"

def num_cosmetica():
    for n in range(1,1000):
        yield f"C - {n}"

p = num_perfumeria()
f = num_farmacia()
c = num_cosmetica()

def decorador(rubro):
    print("\n" + "*" * 23)
    print("Su numero es: ")
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))
    print("Aguarde a ser atendido")
    print("\n" + "*" * 23)
