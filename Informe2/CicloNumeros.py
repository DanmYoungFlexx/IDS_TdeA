n = int(input("Ingrese un número n: "))

contador = 0

print(f"Números pares entre 0 y {n}:")
for i in range(0, n + 1, 2):
    print(i, end=" ")
    contador += 1
    
    # Cada vez que se impriman 10 números, hacemos un salto de línea
    if contador == 10:
        print()
        contador = 0

print("\nFin del programa")