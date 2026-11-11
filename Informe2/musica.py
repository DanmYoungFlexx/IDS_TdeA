genero = input("Ingrese genero: ")

if (genero == "Electronica" or genero == "Pop"):
    anio = int(input("Ingrese su año de nacimiento: "))
    if (anio > 2000 and genero == "Pop"):
        print("Tengo la camisa negra")
    else:
        print("Por siempre Daft punk")
else:
    print("Los únicos géneros buenos son Electronica y Pop")

print("Fin programa")