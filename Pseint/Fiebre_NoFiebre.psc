SubProceso  Fiebre ( temp )
	
	Si temp>=38 Entonces
	   Escribir "la persona tiene fiebre";
	SiNo
		Escribir "la persona no tiene Fiebre";
	FinSi
	
FinSubProceso


Proceso Fiebre_NoFiebre
	
	Definir temp Como Entero;
	
	Escribir "Digite la temperatura";
	
	Leer temp;
	
	Fiebre(temp); 
	
FinProceso
	
	
	
	
