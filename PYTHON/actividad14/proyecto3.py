#Diseñe una app que permita almacenar la información de los clientes de una empresa. Los clientes se guardarán en un diccionario llamado clientes. Los datos deben ser ingresado por el usuario: identificación del cliente, nombre, dirección, teléfono, correo y empresa. La app debe preguntar al usuario por una opción de menú.

#Añadir cliente.
#Mostrar cliente.
#Eliminar cliente.
#Salir o finalizar 

cliente={}
op= ""

while op!=4:
    
    if op==1:
      identificacion=int (input("Digite su Identificacion: "))
      nombre=input("Escriba su Nombre: ")
      direccion=input("Escriba su Direccion: ")
      telefono=int(input("Digite su Telefono: "))
      correo=input("Escriba su Correo: ")
      empresa=input("Escriba el nombre de su Empresa: ")

      cliente={
        "identificacion":identificacion,
        "nombre":nombre,
        "direccion":direccion,
        "telefono":telefono,
        "correo":correo,
        "empresa":empresa}
    if op==2:
       print("Informacion del Cliente")
       print("-----------------------")
       print("Identificacion:",cliente["identificacion"])
       print("Nombre Completo:",cliente["nombre"])
       print("Direccion:",cliente["direccion"])
       print("Telefono:",cliente["telefono"])
       print("Correo:",cliente["correo"])
       print("Empresa:",cliente["empresa"])
    if op==3:
       del cliente["identificacion"]
       print("Cliente Eliminado Con Exito!")
    if op==4:
       exit()

    print("----MENU----")
    print("1-AÑADIR CLIENTE")
    print("2-MOSTRAR CLIENTE")
    print("3-ELIMINAR CLIENTE")
    print("4-SALIR")
    op=int(input("Seleccione una opcion: "))


 

