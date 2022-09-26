"1. Suma"
"2. Resta"
"3. Multiplicacion"
"4. Division" 

var op;
var n1, n2, resultado

op= parseInt(prompt(" Escoja una opcion del menú: "));

switch (op) {
    case 1:
       n1=parseInt(prompt ("Digite el primer numero: ")); 
       n2=parseInt(prompt ("Digite el segundo numero: "));
       resultado=n1+n2
       document.write("La suma de : "+n1+" + "+n2+ " es: "+resultado)
    
    break;
    case 2:
       n1=parseInt(prompt ("Digite el primer numero: ")); 
       n2=parseInt(prompt ("Digite el segundo numero: "));
       resultado=n1-n2
       document.write("La Resta : "+n1+" - "+n2+ " es: "+resultado)
    

    break;
    case 3:
       n1=parseInt(prompt ("Digite el primer numero: ")); 
       n2=parseInt(prompt ("Digite el segundo numero: "));
       resultado=n1*n2
       document.write("La Multiplicacion de : "+n1+" * "+n2+ " es: "+resultado)
    

    break;
    case 4:
       n1=parseFloat(prompt ("Digite el primer numero: ")); 
       n2=parseFloat(prompt ("Digite el segundo numero: "));
       resultado=n1/n2
       document.write("La Division de : "+n1+" / "+n2+ " es: " +resultado)

       break;
    

    default:
        document.write("Escoja una opcion valida")
        break;
}