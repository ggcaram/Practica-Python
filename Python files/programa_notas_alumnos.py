print("Programa de evaluacion de notas de alumnos")

nota_alumno=input()

def evaluacion(ingresar_nota_alumno):
	valoracion="aprobado"
	if ingresar_nota_alumno<5:
		valoracion="reprobado"
	return valoracion

print(evaluacion(int(nota_alumno)))