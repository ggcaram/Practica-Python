print("Programa de evaluacion de notas de alumnos")

nota_alumno=input()

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspendido"
	return valoracion

print(evaluacion(int(nota_alumno)))