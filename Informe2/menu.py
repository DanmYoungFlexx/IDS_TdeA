menu = {
    '1': 'Hamburguesa',
    '2': 'Pizza',
    '3': 'Perro caliente',
    '4': 'Salchipapas',
    '5': 'Pollo'
}

precios = {
    '1': 5.00,
    '2': 8.00,
    '3': 3.00,
    '4': 2.00,
    '5': 4.00
}

opcion = ''

while opcion != '0':
    print("\n--- Bienvenido al menú de comida rápida ---")
    print("1. Hamburguesa")
    print("2. Pizza")
    print("3. Perro caliente")
    print("4. Salchipapas")
    print("5. Pollo")
    print("0. Salir")
    
    opcion = input("Ingrese el número del producto que desea ordenar (0 para salir): ")
    
    if opcion == '1':
        print(f"Ha ordenado una {menu[opcion].lower()}, su valor es ${precios[opcion]:.2f}.\n")
    elif opcion == '2':
        print(f"Ha ordenado una {menu[opcion].lower()}, su valor es ${precios[opcion]:.2f}.\n")
    elif opcion == '3':
        print(f"Ha ordenado un {menu[opcion].lower()}, su valor es ${precios[opcion]:.2f}.\n")
    elif opcion == '4':
        print(f"Ha ordenado unas {menu[opcion].lower()}, su valor es ${precios[opcion]:.2f}.\n")
    elif opcion == '5':
        print(f"Ha ordenado un {menu[opcion].lower()}, su valor es ${precios[opcion]:.2f}.\n")
    elif opcion == '0':
        print("¡Gracias por su compra! Saliendo...")
    else:
        print("Opción no válida. Por favor, intente de nuevo.\n")