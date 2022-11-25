#creamos las listas (vacías al comienzo)

nombres=[]
identificacion=[]
correos=[]
numeros=[]
direcciones=[]
fechas=[]
lugares=[]
#Definimos un tamaño para las listas 
#Lo puedes cambiar si quieres 
tamaño= int(input("tamaño de la lista: "))
#Recorremos la lista hasta el yamaño definido
for i in range(tamaño):
    print("ingrese los datos del aprendiz ", i + 1)
    nombre= input("Nombre del aprendiz: ")
    id= input("N° de Identificacion: ")
    correo= input("Correo Electronico: ")
    numero= int(input("Numero de Telefono: "))
    direccion=input("Direccion de Residencia: ")
    fecha= int(input("Fecha de Nacimiento: "))
    lugar= input("Lugar de Nacimiento: ")
    nombres.append(nombre)
    identificacion.append(id)
    correos.append(correo)
    numeros.append(numero)
    direcciones.append(direccion)
    fechas.append(fecha)
    lugares.append(lugar)

print("Informacion del aprendiz")
print("Los aprendices son: ")
#Ahora mostramos las listas 
for i in range(tamaño):
    print("---------------------------------------------------")
    print("Nombre:", nombres[i])
    print("Identificacion: ",identificacion[i])
    print("Correo: ", correos[i])
    print("Numero: ", numeros[i])
    print("Direccion: ",direcciones[i])
    print("Fecha: ", fechas[i])
    print("Lugar: ", lugares[i])