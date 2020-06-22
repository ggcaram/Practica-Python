def generaPares(limite):
	num=1

	miLista=[]

	while num <limite:
		miLista.append(num*2)

		num=num+1

	return miLista

print(generaPares(10))

def generaPares2(limite2):
	
	num2=1

	while num2<limite2:

		yield num2*2

		num2=num2+1

devuelvePares=generaPares2(10)

print(next(devuelvePares))

print("La primera llamada muestra el primer numero del array: ")

print(next(devuelvePares))

print("La segunda llamada muestra el segundo numero del array: ")

print(next(devuelvePares))

print("La tercera llamada muestra el tercera numero del array: ")