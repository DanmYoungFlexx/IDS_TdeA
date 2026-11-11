Algoritmo prom
	Definir matematicas, castellano, ingles, sociales, promedio Como Real;
	
	Imprimir ("ingrese la nota de matematicas: ");
	
	leer matematicas;
	
	Imprimir ("ingrese la nota de castellano: ");
	
	Leer castellano;
	
	Imprimir ("ingrese la nota de ingles: ");
	
	Leer ingles;
	
	Imprimir ("ingrese la nota de sociales: ");
	
	leer sociales;
	
	promedio <- (matematicas+castellano+ingles+sociales)/4;
	
	Imprimir (promedio);
	
	Si (promedio > 4.5) Entonces
		
		Imprimir ("Puedes acceder a la beca");
		
		SiNo
			
			Imprimir ("Aún no puedes acceder a la beca, intenta el otro semestre");
			
			FinSi


	
FinAlgoritmo
