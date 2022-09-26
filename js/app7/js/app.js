var salario, descuento, monto;

salario=parseFloat(prompt("Ingrese su salario: "));

descuento=salario*0.05;
monto=salario*0.95;

document.write("El descuento es: "+descuento+" y el resto total de dinero es: "+monto);


