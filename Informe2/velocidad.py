velocidad = float(input("Ingrese la velocidad (km/h): "))
zona = input("Ingrese la zona (escolar, urbana, rural, nacional): ")

# Definir límites según la zona
if zona == "escolar":
    limite = 30
elif zona == "urbana":
    limite = 60
elif zona == "rural":
    limite = 80
elif zona == "nacional":
    limite = 100
else:
    limite = None

# Validar y mostrar resultado
if limite is None:
    print("Zona no válida.")
elif velocidad <= limite:
    print(f"¡Vas bien! Estás dentro del límite de {limite} km/h.")
else:
    print(f"¡Infringes la norma! Superas el límite de {limite} km/h para esta zona.")