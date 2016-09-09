#coding=utf-8


print("Hola mundo")

Nombre1 = input("Nombre de la primera persona: ")
if(Nombre1=="Dario"):
	print("Aaa el bronze.")
else:
	print("Hola, bienvenido %s." % Nombre1)


Edad1 = int(input("Edad de la primer persona: "))

Nombre2 = input("Nombre de la segunda persona: ")
print("Hola %s, bienvendio." % Nombre2)

Edad2 = int(input("Edad de la segunda persona: "))

if(Edad1>Edad2):
	print("%s eres mayor que %s." % (Nombre1, Nombre2))
elif(Edad1<Edad2):
	print("%s eres mayor que %s." % (Nombre2, Nombre1))
else:
	print("%s y %s tienen la misma edad." % (Nombre1, Nombre2))
	
