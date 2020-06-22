print("Programa de tranferencia ciudadania española: ")
print("Opciones de parentesco: padre - madre - abuelo - abuela")
parentesco=input("Escribe el parentesco con el ciudadano: ")

familia=parentesco.lower()

if parentesco in ("padre","madre","abuelo","abuela"):
	print("Tu "+ familia +" te habilita para sacar la ciudadania española")
else:
	print("No cumplis con las condiciones para la trasnferencia")
