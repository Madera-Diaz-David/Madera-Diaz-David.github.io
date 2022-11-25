#Diseñe una app y almacene los datos de una tienda de películas, para ello debe crear las siguientes listas vacías

titulos=[]
generos=[]
duraciones=[]
protagonistas=[]
años=[]
precios=[]
idiomas=[]

#Definimos un tamaño para las listas 
#Lo puedes cambiar si quieres 

tamaño= int(input("tamaño de la lista: "))
#Recorremos la lista hasta el yamaño definido
for i in range(tamaño):
    print("Ingrese los datos de la pelicula: ", i + 1)
    titulo= input("Titulo de la Pelicula: ")
    genero= input("Genero de la Pelicula: ")
    duracion= input("Duracion de la Pelicula: ")
    protagonista= input("protagonista de la pelicula: ")
    año= input("Año de la pelicula: ")
    precio= input("Precio de la Pelicula: ")
    idioma= input ("Idioma de la pelicula: ")

    titulos.append(titulo)
    generos.append(genero)
    duraciones.append(duracion)
    protagonistas.append(protagonista)
    años.append(año)
    precios.append(precio)
    idiomas.append(idioma)

    print("Datos de la pelicula: ")
    #Ahora mostramos las listas 
    for i in range(tamaño):
        print("---------------------------------------------------")
        print("Titulo: ", titulos[i])
        print("Genero: ", generos[i])
        print("Duracion: ", duraciones[i])
        print("Protagonista: ", protagonistas[i])
        print("Año: ", años[i])
        print("Precio: ", precios[i])
        print("Idioma: ", idiomas[i])
    


