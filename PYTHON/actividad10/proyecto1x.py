#creamos las listas (vacías al comienzo)

nombres=[]
#Definimos un tamaño para las listas 
#Lo puedes cambiar si quieres 
tamaño= int(input("tamaño de la lista: "))
#Recorremos la lista hasta el yamaño definido
for i in range(tamaño):
    print("ingrese los datos del aprendiz ", i + 1)
    nombre= input("Nombre del aprendiz: ")
    nombres.append(nombre)
print("Los aprendices son: ")
#Ahora mostramos las listas 
for i in range(tamaño):
    print("---------------------------------------------------")
    print("Nombre:", nombres[i])