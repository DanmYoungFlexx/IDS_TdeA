correo = "danipiemol@gmail.com"
contraseña = "12345678"

palabra = input("Digite su correo electronico: ")

existe = correo.find(palabra) != -1

if existe:
    contraseña_ingresada = input(f"Digite su contraseña: ")
    if contraseña_ingresada == contraseña:
        print(f"Contraseña correcta, bienvenido")
    else:
        print(f"Contraseña incorrecta, intente nuevamente")
else:
    print(f"Verificacion de correo fallida, por favor ingrese un correo valido")
    
    