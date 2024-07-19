def suma(**kwargs):

    # print(type(kwargs))

    total = 0

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=3,y=5,z=2))


def suma_mixta(num1, num2, *args, **kwargs):

    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

# suma_mixta(15,50,100,200,300,400,x="Uno", y="Dos", z="Tres")

# Alternativa de uso

args = [100,200,300,400]

kwargs = {"x":"Uno","y":"Dos","z":"Tres"}

suma_mixta(15,50,*args,**kwargs)
