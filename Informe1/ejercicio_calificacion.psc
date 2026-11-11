Algoritmo ejercicio_calificacion
	DEFINIR calificacion Como REAL;
	
	calificacion <- 0;
	
	ESCRIBIR "Ingrese la calificacion del alumno: ";
	
	LEER calificacion;
	
	SI (calificacion >= 8) ENTONCES
		
		ESCRIBIR "El alumno está APROBADO";
		
	SINO
		
		ESCRIBIR "El alumno está REPROBADO";
		
	FINSI
FinAlgoritmo
