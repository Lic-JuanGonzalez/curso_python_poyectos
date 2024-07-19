#Version anterior a la 3.10 no existe un switch
serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe ese producto")

# Nueva funcionalidad
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")

cliente = {'nombre':'Juan',
           'edad':23,
           'ocupacion':'programador'}

pelicula = {'titulo': 'Matrix',
            'ficha_tecnica':{'protagonista':'Keanu Reaves',
                              'director':'Lana y Lily Wachowsky'}}

elementos = [cliente, pelicula, 'libros']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista':protagonista,
                                'director':director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se que es esto")

