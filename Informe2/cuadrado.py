LadoCuadrado = float(int(input("Ingrese el lado del cuadrado: ")))

if LadoCuadrado > 0:
    Area = LadoCuadrado * LadoCuadrado
    print("El area del cuadrado es: " + str(Area))
else:
    print("El lado no puede ser menor o igual a 0")
    
print("Fin del programa")