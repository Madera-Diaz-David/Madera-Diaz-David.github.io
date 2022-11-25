#Formula imc

peso= int(input("ingrese el peso de la persona: "))
estatura= float(input("ingrese la estatura de la persona: "))

imc=peso/(estatura*estatura)

if imc<=18.5:
    print("La persona tiene bajo peso ")
elif imc>=18.5 and imc<=24.9:
    print("La persona tiene un peso normal ")
elif imc>=25 and imc<=29.9:
    print("La persona tiene sobrepeso ")
elif imc>=30 and imc<=34.9:
    print("La persona tiene obesidad 1")
elif imc>=35 and imc<=39.9:
    print("La persona tiene obesidad 2")
elif imc>=40 and imc<=49.9:
    print("La persona tiene obesidad 3")
elif imc>50:
    print("La persona tiene obesidad 4")