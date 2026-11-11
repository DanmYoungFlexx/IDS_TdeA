def cifrado(texto, desplazamiento):
    # Definimos el abecedario (puedes añadir la 'ñ' si quieres)
    abc = "abcdefghijklmnñopqrstuvwxyz"
    resultado = ""

    # Pasamos el texto a minúsculas para simplificar
    for letra in texto.lower():
        if letra in abc:
            # Buscamos la posición actual de la letra
            posicion_actual = abc.index(letra)
            # Sumamos el desplazamiento (el % 26 evita que nos salgamos del abecedario)
            nueva_posicion = (posicion_actual + desplazamiento) % 26
            # Añadimos la nueva letra al resultado
            resultado += abc[nueva_posicion]
        else:
            # Si es un espacio, número o signo, lo dejamos igual
            resultado += letra

    return resultado

print(cifrado("Daniel", 3))  # Imprime: krdo pxqgr
