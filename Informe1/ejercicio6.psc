Algoritmo ejercicio6
	Definir KmRecorrido, precio, dinero, horas, minutos Como Real
	
	Definir consumoGasoTotal, consumoGasoKm, consumoGaso100Km Como Real
	
	Definir precioGasoKm, precioGaso100Km, velKmHora, velMetrSeg Como Real
	
	Escribir 'Ingrese el total de km recorridos'
	
	Leer KmRecorrido
	
	Escribir 'Ingrese el precio de la gasolina (por litro)'
	
	Leer precio
	
	Escribir 'Ingrese el dinero gastado en el viaje'
	
	Leer dinero
	
	Escribir 'Ingrese el tiempo de horas del viaje'
	
	Leer horas
	
	Escribir 'Ingrese el tiempo adicional de minutos'
	Leer minutos

	
	consumoGasoTotal <- dinero/precio
	
	consumoGasoKm <- consumoGasoTotal/KmRecorrido
	consumoGaso100Km <- consumoGasoKm*100
	
	precioGasoKm <- consumoGasoKm*precio
	
	precioGaso100Km <- precioGasoKm*100
	
	velKmHora <- KmRecorrido/(horas+(minutos/60))
	
	velMetrSeg <- (KmRecorrido*1000)/((horas*3600)+(minutos*60))
	
	
	Escribir 'El consumo de gasolina en litros por 100 kilometros es: ', consumoGaso100Km
	
	Escribir 'El consumo de gasolina en euros por 100 kilometros es: ', precioGaso100Km
	
	Escribir 'El consumo de gasolina en litros por kilometro es: ', consumoGasoKm
	
	Escribir 'El consumo de gasolina en euros por kilometro es: ', precioGasoKm
	
	Escribir 'La velocidad media de Km/Hora es: ', velKmHora
	
	Escribir 'La velocidad media de metros/seg es: ', velMetrSeg
	

	
FinAlgoritmo
