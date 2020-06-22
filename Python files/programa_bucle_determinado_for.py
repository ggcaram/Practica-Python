for numeros in [1,2,3]:
	print(numeros)

#Funcion, se ejecuta porcada letra del in
for z in "pepitalapistolera":
	print("Ingresa el mail ", end=" ")

#Recorre todo el string y corrobora si hay un arroba
nombre=0
tunombre= input("Como te llamas? ")

for z in tunombre:
	if (z=="D" or z=="A" or z=="C"):
		nombre=nombre+1

if nombre==3:
	print("Sos un salame")
else:
	print("No es ningun salame")

