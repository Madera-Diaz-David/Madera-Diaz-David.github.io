//Aplicacion para evaluar Mayor o Igual a 10 
var n;

n=parseInt(prompt("Digite el numero entero: "));

//Evaluar mayor o menor a 10
if (n>10) {
    document.write("El numero "+n+" es mayor que 10 <img src='img/bloques-numericos.png' width='30px' height='30px'");
    
} else {
    document.write("El numero "+n+" es menor que 10 <img src='img/herramienta-de-edicion.png' width='30px' height='30px' ");
    
}