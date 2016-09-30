#coding=utf-8
#Programa para pedir una orden

precio = 0
orden = 1
print ("Hola, bienvenido a Carl´s Jr")
print ("""
Menu:
1. Famous Star ($90)
2. Papas grandes ($40)
3. Santa fe ($100)
4. Soda grande ($30)
5. Salir""") 

while (orden<5):	
	orden = int(input("¿Que va a pedir?"))
	
	
	
	if (orden == 1): 
		precio = precio + 90
	elif (orden == 2):
		precio = precio + 40
	elif (orden == 3): 
		precio = precio + 100
	elif (orden == 4): 
		precio = precio + 30


	print("Su precio es un total de $%s " %(precio))
	
else:
	print("gracias por su visita")

