#Diseñe una app que permita al usuario ingresar fruta y el precio unitario, cantidad y lo almacene en un diccionario llamado factura. Después debe mostrar un mensaje concatenado donde aparece el nombre de la fruta su valor, la cantidad y el total

fruta=input("Ingrese la Fruta: ")
precio=int(input("Digite el Precio: "))
cantidad=int(input("Digite la Cantidad: "))
total=precio*cantidad

factura={"Fruta":fruta,"Precio":precio,"Cantidad":cantidad, "Total":total}

print("El Nombre de la fruta es: ",factura["Fruta"], "y tiene un precio de: ",factura["Precio"], "con una cantidad de: ",factura["Cantidad"], "y su total es de: ", factura["Total"])