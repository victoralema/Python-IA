##21310193 Vcitor Eduardo Aleman Padilla
variable = "Correcto."##creamos una varible y le asignamos valor

try:##probamos un bloque para buscar errores
	print(variable)##imprimimos la varible
except:##si no encuentra varibale declarada entra aca(manejamos el error)
	print("La variable no está declarada.")##imprime informacion

##ahora uno sin variable declarada
try:
	print(va)
except:
	print("La variable no está declarada.")
