#App que al ingresar un numero entero positivo, muestre todos los numeros impares ingresados

n=int(input("Digite un numero: "))
for i in range (1,n,2):
    print(i, end=", ")

