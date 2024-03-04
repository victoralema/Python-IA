##21310193 Victor Eduardo Aleman Padilla
##Se usara el comparador if,else y elif
edad = int(input('¿Cuál es tu edad?\n'))##Creamos una variable de entrada de datos e imprimimos texto o instruccion
if edad <= 0:##Evaluamos el condicional, si es verdadero ejecutara y si no saltara al siguiente
	print('Nadie puede tener esa edad.')##imprimimos
elif edad >= 1 and edad <= 18:##Evaluamos el condicional, si es verdadero ejecutara y si no saltara al siguiente
	print('Eres menor de edad.')##imprimimos
elif edad > 18 and edad <= 45:##Evaluamos el condicional, si es verdadero ejecutara y si no saltara al siguiente
	print('Eres mayor de edad.')##imprimimos
elif edad > 45 and edad <= 100:##Evaluamos el condicional, si es verdadero ejecutara y si no saltara al siguiente
	print('Eres mayor de edad, pero ya no tan joven.')##imprimimos
elif edad > 100 and edad <= 120:##Evaluamos el condicional, si es verdadero ejecutara y si no saltara al siguiente
	print('Eres muy mayor.')##imrpimimos
else:##Si no es ninguna de las anteriores, se ejecuta el else
	print('Edad no válida.')##imprimimos
