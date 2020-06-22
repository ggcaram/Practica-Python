print("Programa de evaluacion de PBI:")

pbi_usa=int(input("Ingresa el PBI de USA: "))
print("PBI de USA:: " + str(pbi_usa))
pbi_brasil=int(input("Ingresa el PBI de Brasil: "))
print("PBI de Brasil: " + str(pbi_brasil))
pbi_argentina=int(input("Ingresa el PBI de Argentina: "))
print("PBI de Argentina: " + str(pbi_argentina))
pbi_somalia=int(input("Ingresa el PBI de Somalia: "))
print("PBI de Somalia: " + str(pbi_somalia))

if pbi_usa>pbi_brasil>pbi_argentina>pbi_somalia:
	print("Las mediciones son correctas")
else:
	print("Error de medicion")
