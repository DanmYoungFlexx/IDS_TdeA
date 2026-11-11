Algoritmo ejercicio7
	Definir nombre Como Cadena
	Definir basico Como Real
	Definir hijos Como Entero
	Definir bonificacion, final Como Real
	Escribir "Ingrese el nombre del trabajador"
	Leer nombre
	Escribir "Ingrese el sueldo base"
	leer basico
	Escribir "Ingrese el numero de hijos"
	Leer hijos
	bonificacion <- 0
	si hijos > 0
		
		bonificacion <- basico * 0.07
		
		FinSi
		
		final <- basico + bonificacion
		
		Escribir "La bonificacion es: ", bonificacion
		
		Escribir "El sueldo final es: ", final
	
	
FinAlgoritmo
