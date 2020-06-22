print("Programa de evaluacion de edad")

ingresar_edad=int(input("Ingresa tu edad: "))
if 18<ingresar_edad<22:
	print("Podes pasar")
elif 0< ingresar_edad <18:
	print("No podes pasar")
else:
	print("Edad incorrecta")
