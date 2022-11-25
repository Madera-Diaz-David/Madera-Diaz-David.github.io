#Diseñe una app que permita al usuario ingresar nombre, edad, dirección y teléfono; estos datos se deben almacenar en un diccionario llamado persona. Estos datos se deben mostrar por pantalla de forma concatenada

nombre=input("Ingrese su Nombre: ")
edad=input("Digite su Edad: ")
direccion=input("Digite su Direccion: ")
telefono=input("Digite su Telefono: ")

persona={"nombre":nombre,"edad":edad,"direccion":direccion,"telefono":telefono}

print(persona["nombre"], "Tiene: ", persona["edad"],"Años", "y vive en: ", persona["direccion"], "y su numero de telefono es ", persona["telefono"])


