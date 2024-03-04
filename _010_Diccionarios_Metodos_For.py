##21310193 Victor Eduardo Aleman Padilla
##Diccionarios y ciclo for y metodos
teclado1 = {
	'Categoría': 'Teclados',##categoria
	'Modelo': 'HyperX Alloy FPS Pro',##Modelo
	'Precio': '89,99'##precio
}##Creamos diccionario con elementos precargados

teclado2 = {
	'Categoría': 'Teclados',##categoria
	'Modelo': 'Corsair K55 RGB',##Modelo
	'Precio': '59,99'##precio
}##Creamos diccionario con elementos precargados

for x in teclado2:##iniciamos for para imprimir teclado 2
	print(teclado2[x])##Imprimimos los datos de nuestro segundo diccionario

del teclado1['Precio']##borramos un elemento de nuestro diccionario
print(teclado1)##mostramos diccionario

teclado1['Color'] = 'Negro'##añadimos elemento a nuestro diccionario
print(teclado1)##mostramos diccionario
