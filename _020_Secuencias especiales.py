##21310193 Victor Eduardo Aleman Padilla
##Secuencias especiales
import re##importamos caracteres

texto = "Se acerca el invierno."##guardamos en una varible recien creada un texto
buscar = re.findall("vierno.$", texto)##buscamos coincidencias de palabras que contengan el texto
if buscar:##Si la condicion en cuentra algo, entra
	print("Hay al menos una coincidencia.")##imprimimos resultado
else:##Si no hay ninguna coincidencia ejecutamos
	print("No hay coincidencias.")##imprimimos resultado
buscar1 = re.findall("^Se acerca", texto)
if buscar1:
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")

