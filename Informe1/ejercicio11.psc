Algoritmo ejercicio11
	Definir sexo, categoria Como Cadena
	
	Definir edad Como Entero
	
	Escribir 'Ingrese el sexo del postulante (Femenino o Masculino)'
	
	Leer sexo
	
	Escribir 'Ingrese la edad del postulante'
	
	Leer edad
	
	Si sexo='Femenino' Entonces
		
		Si edad<23 Entonces
			
			categoria <- 'FA'
			
			SiNo
				
				categoria <- 'FB'
				
				FinSi
				
				SiNo
					
					Si edad<25 Entonces
						
						categoria <- 'MA'
						
						SiNo
							
							categoria <- 'MB'
							
							FinSi
							
							FinSi
							
							Escribir 'La categoria del postulante es: ', categoria
FinAlgoritmo
