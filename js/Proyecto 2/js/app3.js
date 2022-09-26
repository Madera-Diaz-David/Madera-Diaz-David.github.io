//Aplicacion para evaluar numero Positivo y Negativo
var n;

n=parseInt(prompt("Digite el numero entero: "));

//Evaluar positivo negativo
if (n>=0) {
    document.write("El numero "+n+" es positivo    <img src='img/agregar.png' width='30px' height='30px'"); 
    
} else {
    document.write("El numero "+n+" es negativo <img src='img/menos.png' width='30px' height='30px'");  
    
}