#Diseñe una app que almacene los datos de un vehículo, para ello debe crear las siguientes listas vacías, alimentarlas y mostrar por pantalla

#creamos las listas (vacías al comienzo)

marcas=[]
modelos=[]
colores=[]
combustibles=[]
cilindrajes=[]
precios=[]

#Definimos un tamaño para las listas 
#Lo puedes cambiar si quieres 
tamaño= int(input("tamaño de la lista: "))
#Recorremos la lista hasta el yamaño definido
for i in range(tamaño):
    print("Ingrese los datos del Vehiculo: ", i + 1)
    marca= input("Marca del Vehiculo: ")
    modelo= int (input("Modelo del Vehiculo: "))
    color= input("Color del Vehiculo: ")
    combustible= input("Combustible del Vehiculo: ")
    cilindraje= int(input("Cilindraje del Vehiculo: "))
    precio= int(input("Precio del Vehiculo: "))

    marcas.append(marca)
    modelos.append(modelo)
    colores.append(color)
    combustibles.append(combustible)
    cilindrajes.append(cilindraje)
    precios.append(precio)

    print("Datos del vehiculo: ")
    #Ahora mostramos las listas 
    for i in range(tamaño):
          print("---------------------------------------------------")
          print("Marca: ", marcas[i])
          print("Modelo: ", modelos[i])
          print("Color: ", colores [i])
          print("Combustible: ", combustibles[i])
          print("Cilindraje: ", cilindrajes[i])
          print("Precio: ", precios[i])

  
