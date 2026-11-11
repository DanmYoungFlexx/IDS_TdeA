Algoritmo ejercicio8
	Definir edad Como Entero
	Definir valorEntrada Como Real
	
	Escribir "Ingrese el valor de la entrada"
	
	Leer valorEntrada
	
	Escribir "Ingrese la edad del cliente"
	
	Leer edad
	
	Si edad < 10
		
		valorEntrada <- valorEntrada - (valorEntrada * 0.25)
		
		FinSi
		
		Escribir "El valor a pagar por la entrada el circo es de: " , valorEntrada
FinAlgoritmo
