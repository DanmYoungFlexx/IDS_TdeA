dia = input("Ingrese el día de la semana: ")
producto = input("Ingrese el producto (fruver, carnes, vinos): ")
valor = float(input("Ingrese el valor del producto: "))

descuento_porcentaje = 0

# Evaluar condiciones por día y producto[cite: 6]
if dia == "lunes":
    if producto == "fruver":
        descuento_porcentaje = 30
elif dia == "martes":
    if producto == "carnes":
        descuento_porcentaje = 30
elif dia == "jueves":
    if producto == "vinos":
        descuento_porcentaje = 30
elif dia == "miercoles":
    if producto == "carnes":
        descuento_porcentaje = 15
    elif producto == "fruver":
        descuento_porcentaje = 10
    elif producto == "vinos":
        descuento_porcentaje = 5
elif dia == "viernes":
    if producto == "vinos":
        descuento_porcentaje = 15
    elif producto == "fruver":
        descuento_porcentaje = 10
    elif producto == "carnes":
        descuento_porcentaje = 5

costo_total = valor - (valor * descuento_porcentaje / 100)

print(f"Descuento: {descuento_porcentaje}%")
print(f"Costo Total: {int(costo_total)}")