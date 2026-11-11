Algoritmo ejercicio_intereses
	Definir intereses Como Real
	Definir dias, capital, ganancias Como Entero
	intereses <- 0.02
	dias <- 0
	capital <- 0
	ganancias <- 0
	Escribir "Digite el capital"
	Leer capital
	Escribir "Digite los dias del mes"
	Leer dias
	ganancias <- (capital*dias) * intereses
	
	Escribir "La ganancia es: ", ganancias
FinAlgoritmo
