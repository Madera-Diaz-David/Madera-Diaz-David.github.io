var a,b,i

i=1

a=parseInt(prompt("ingrese le valor inicial"));
b=parseInt(prompt("ingrese el valor final"));

for (i=a; i<=b; i++) {
    if (i%2==0) {
    document.write (i)  
    
 }else{
    document.write("<br>")
}
}