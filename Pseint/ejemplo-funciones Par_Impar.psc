SubProceso  par ( n )
	
	Si (n mod 2)=0 Entonces
		Escribir "El numero ", n, " es par";
	SiNo
		Escribir "El numero ", n, " es impar";
	FinSi

	
FinSubProceso




Proceso Par_Impar
	
	Definir n Como Entero;
	
	Escribir "Digite el numero ";
	
	Leer n;
	
	par(n);
	
	
FinProceso
