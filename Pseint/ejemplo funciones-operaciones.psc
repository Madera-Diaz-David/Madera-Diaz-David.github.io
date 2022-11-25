
SubProceso Sumar ( n1,n2 )
	
	Escribir "la suma de: ",n1, " + ",n2," = ", n1+n2;
	
FinSubProceso

SubProceso restar ( n1,n2 )
	
	Escribir "la resta de: ",n1, " - ",n2," = ", n1-n2;
	
FinSubProceso


SubProceso multiplicar ( n1,n2 )
	
	Escribir "la multiplicacion de: ",n1, " * ",n2," = ", n1*n2;
	
FinSubProceso	

SubProceso dividir ( n1,n2 )
	
	Escribir "la division de: ",n1, " / ",n2," = ", n1/n2;
	
FinSubProceso	



Proceso operaciones
	
	Definir a,b Como Entero;
	
	Escribir "Digite el primer numero: ";
	Leer a;
	
	Escribir "Digite el segundo numero: ";
	Leer b;
	
	sumar(a,b);
	restar(a,b);
	multiplicar(a,b);
	dividir(a,b);
	
	
	
	
FinProceso
