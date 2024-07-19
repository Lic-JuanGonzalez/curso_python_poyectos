def suma(a,b):
    return a+b

print(suma(5,6,))

def suma_args(*args):
    """total = 0

    for arg in args:
        total += arg

    return total

    funcional de la misma manera

    """

    return sum(args)


