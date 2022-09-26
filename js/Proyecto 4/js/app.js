var peso, estatura, imc

peso=parseFloat(prompt("Digite el peso en Kg: "));
estatura=parseFloat(prompt("Digite la estatura en Mts: "));

imc= peso/(estatura*estatura);

if (imc<18.5) {
    document.write("bajo peso  <img src='img/bajo peso.jpg' alt='bajo peso' width='30px' height='30px'> ");
}
else if(imc>=18.5 && imc<24.9){
    document.write("Peso Normal <img src='img/peso normal.jpg' alt='peso normal' width='30px' height='30px'> ");

}
else if(imc>=25 && imc <29.9){
    document.write("Sobre peso <img src='img/Sobrepeso.webp' alt='Sobre peso' width='30px' height='30px'> ");
}

else if(imc>=30 && imc <34.9){
    document.write("obesidad 1 <img src='img/obecidad 1.webp' alt='obecidad 1' width='30px' height='30px'>")
}

else if(imc>=35 && imc <39.9){
    document.write("Obesidad 2 <img src='img/obecidad 2.png' alt='obecidad 2' width='30px' height='30px'>")
}

else if(imc>=40 && imc <49.9){
    document.write("Obesidad 3 <img src='img/obecidad 3.jpg' alt='obecidad 3' width='30px' height='30px'>")
}

else if(imc>=50){
    document.write("Obesidad 4 <img src='img/obecidad 4.png' alt='obecidad 4' width='30px' height='30px'>")
}

else {
    document.write("Escriba los valores numericos esperados")
}



