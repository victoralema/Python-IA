##21310193 Victor Eduardo Aleman Padilla
##Ciclo while for e if
x = 1##Creamos varible para contador

while x <= 10:##Evaluamos la conmdicion y si es verdadera el ciclo saldra hasta que if sea verdadero
	print(x)##imprimimos valor del contador
	if x == 10:##evaluamos contador para salir del while
		break##rompe el ciclo
	x += 1##Se le agrega 1 al contador por cada ciclo

for i in range(5,10):##Se ejecuta el ciclo hasta que el for llegue de un rango de 5 a 10
	print("For",i)##Se imprime valor del contador del for
