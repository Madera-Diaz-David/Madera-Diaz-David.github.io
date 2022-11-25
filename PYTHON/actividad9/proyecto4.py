#ELIMINAR ELEMENTOS DE LAS LISTAS CON LAS DOS FORMAS:pop,remove

#Array lista: añade un elemento al vector
frutas= ["apple", "banana", "cherry"]
#añadimos un elemento a la lista
frutas.append("orange")
#Eliminar elementos de las lista con la forma:pop
frutas.pop(1) 
#rrecorremos la lista
for x in frutas:
    print(x)
#Definimos la longitud de la lista
longitud=len(frutas)
print("El tamaño o logitud es: ", longitud)


#Listas de libros con 7 posiciones.
Libros= ["Romancero Gitano", "Diario De Un Loco", "Las Metamorfosis", "Edipo Y Rey", "Ramayana", "Cien Años De Soledad", "El Tunel",]
Libros.append("La María")
#Eliminar elementos de las lista con la forma:remove
Libros.remove("Diario De Un Loco") 
for x in Libros:
     print(x)

longitud=len(Libros)
print("El tamaño o logitud es: ", longitud)

#Listas de plantas medicinales con nueve posiciones
Plantas= ["Ginkgo Biloba", "Menta", "Jengibre", "Llanten", "Eucalipto", "Torongil", "Anís", "Sábila", "Perejil"]
Plantas.append("Marihuana")
Plantas.remove("Eucalipto")
for x in Plantas:
    print(x)

longitud=len(Plantas)
print("El tamaño o logitud es: ", longitud)

#Listas de lenguajes de programación con 5 posiciones.
Lenguajes= ["JavaScript", "Python", "C/C++", "PHP", "Java"]
Lenguajes.append("Objective-C")
Lenguajes.remove("Java")
for x in Lenguajes:
    print(x)

longitud=len(Lenguajes)
print("El tamaño o logitud es: ", longitud)

#Listas de colores con ocho posiciones
Colores= ["Rojo", "Azúl", "Amarillo", "Verde", "Naranja", "Morado", "Blanco", "Negro"]
Colores.append("Rosado")
Colores.remove("Blanco")
for x in Colores:
    print(x)

longitud=len(Colores)
print("El tamaño o logitud es: ", longitud)