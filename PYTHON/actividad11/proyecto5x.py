#Diseñe una app que almacene los datos de un sistema de facturación; para ello se deben crear las siguientes listas vacías, alimentarlas y mostrarlas

#creamos las listas (vacías al comienzo)

codigofactura=[]
codigocliente=[]
nombrecliente=[]
fechafactura=[]
descripcionproducto=[]
preciounitario=[]
cantidades=[]
totales=[]


#Definimos un tamaño para las listas 
#Lo puedes cambiar si quieres 

tamaño= int(input("tamaño de la lista: "))
#Recorremos la lista hasta el yamaño definido
for i in range(tamaño):
     print("Ingrese los datos del sistema de facturacion: ", i + 1)
     codigofac= input("Codigo de la Factura: ")
     codigoclient= input("Codigo del Cliente: ")
     nombreclient= input("Nombre del Cliente: ")
     fechafact= input("Fecha de la Factura: ")
     descripcionproduct= input("Descripcion del Producto: ")
     preciouni= int (input("Precio Unitario del Producto: "))
     cantidad= int (input("Cantidad del Producto: "))
    


     codigofactura.append(codigofac)
     codigocliente.append(codigoclient)
     nombrecliente.append(nombreclient)
     fechafactura.append(fechafact)
     descripcionproducto.append(descripcionproduct)
     preciounitario.append(preciouni)
     cantidades.append(cantidad)
     total= preciouni*cantidad
     totales.append(total)
  



print("Datos del Sistema de Facturacion: ")
    #Ahora mostramos las listas 
for i in range(tamaño):
        print("---------------------------------------------------")
        print("Codigo de la Factura: ", codigofactura[i])
        print("Codigo del Cliente: ", codigocliente[i])
        print("Nombre del Cliente: ", nombrecliente[i])
        print("Fecha de la Factura: ", fechafactura [i])
        print("Descripcion del Producto: ", descripcionproducto[i])
        print("Precio Unitario del Producto: ",preciounitario[i])
        print("Cantidad del Prodcuto: ", cantidades[i])
        print("Total del Producto: ", totales[i])