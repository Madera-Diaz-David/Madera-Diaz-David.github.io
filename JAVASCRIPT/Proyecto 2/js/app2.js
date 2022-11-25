//para evaluar si un numero esta entre 10 y 100
var n;

n=parseInt(prompt("digite el numero entero: "));


//Evaluamos el proceso numerico
if (n>=10 && n<=100) {
    document.write("el numero: "+n+ " Esta entre 10 y 100 <img src='img/voto-positivo.png' width='30px' height='30px'>"); 
} else {
    document.write("el numero : "+n+ " no está entre 10 y 100 <img src='img/matematicas.png' width='30px' height='30px'>"); 
}