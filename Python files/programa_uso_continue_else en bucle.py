#continue pass else

for letra in "Phython":

	if letra=="h":
		continue
		#vuelve al principio del bucle e ignora el codigo que sigue

	print("Viendo la letra " + letra)"""


"""nombre="Buenos Aires"

contador=0

for i in nombre:

	if i==" ":
		continue
	contador+=1

print(contador)

class ejemploClase:
	pass # ejemplo de clase asignada para usar despues 

email=input("Introduce tu mail: ")

for i in email:

	if i=="@":

		arroba=True

		break;
"""la instruccion else no esta en el condicional sino en el bucle else,
 por eso seria una condicion en caso de que este no se active"""
else: 
	arroba=False
print(arroba)