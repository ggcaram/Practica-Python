print("Programa de seleccion celular: ")

valor_equipo=int(input("Ingresa el valor de el equipo "))
print(valor_equipo)
ram=int(input("Ingresa RAM equipo "))
print(ram)
año_salida=int(input("Año de salida: "))
print(año_salida)


if valor_equipo<20000 and ram>2 or año_salida>2017:
	print("Es un buen modelo")
else:
	print("No te conviene comprarlo")
