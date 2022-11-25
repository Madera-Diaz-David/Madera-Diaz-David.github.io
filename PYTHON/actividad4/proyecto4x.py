#presion arterial

presion=int(input("Digite la Presion Arterial"))
if presion<90:
	print("la persona tiene una presion arterial baja")
elif presion >=90 and presion <=120:
	print("la persona tiene una presion arterial normal"); 
elif presion >=120 and presion <=139:
	print("la persona tiene una presion arterial prehipertension") 
elif presion >=140 and presion <=159:
	print("la persona tiene una presion arterial alta:hipertension fase 1") 
elif presion >=160:
	print("la persona tiene una presion arterial alta:hipertension fase 2") 	
else:
	print("digite una presion arterial valida")
