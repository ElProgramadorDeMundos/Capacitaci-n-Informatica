#coding=utf-8

import time


password = "guajolotitos"
correcto = 0
intentos = 1


print ("Bienvenido al Centro Educativo Patria")

while (correcto == 0) & (intentos  <= 4):
	intento = input("Introduce tu contraseña:")
	if intento == password:
		correcto = 1
		print("Tu contraseña es correcta")
	else:
		time.sleep (1)
		print("La contraseña es incorrecta")
		intentos = intentos + 1
		if intentos >4:
			print("Has introducido demaciadas contraseñas")
			
