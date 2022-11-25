//Aplicacion para Aprobar o Reprobar
var nota;

nota=parseFloat(prompt("Ingrese la nota del Alumno"));

//Proceso aprobado o reprobado
if (nota>=3) {
    document.write("El alumno aprobó <img src='img/cheque.png' width='30px' height='30px'");
} else {
    document.write("El alumno reprobó <img src='img/boton-x.png' width='30px' height='30px'");
}