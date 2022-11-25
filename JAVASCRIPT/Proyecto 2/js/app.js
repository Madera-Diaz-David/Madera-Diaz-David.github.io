//Aplicacion para evaluar la Fiebre de una persona
var temp ;

//capturar los datos de entrada
temp=parseFloat(prompt ("ingrese su temperatura en °C: "));

//Proceso para evaluar la fiebre
if (temp >=38) {
  document.write("La temperatura "+temp+"°C Indica Fiebre    <img src='img/caliente.png' width='30px' height='30px'>");  
} else {
    document.write("La temperatura "+temp+"°C Indica sin Fiebre    <img src='img/mujer.png' width='30px' height='30px'>");  
}