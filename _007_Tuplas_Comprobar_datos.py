##21310193 Victor Eduardo Aleman Padilla
##comprobar datos de tuplas y listas
entrada = input('Introduce el nombre de un navegador:\n')##Creamos una variable de tipo entrada con una instruccion
navegadores = ['chrome', 'firefox', 'opera', 'safari']##Creamos la lista con 4 elementos
if entrada in navegadores:##Buscamos nuestra entrada en la lista con el condicional si es cierta ejecutamos if
	print('El navegador que buscas está en la lista.')##imprimimos resultados
else:##si el condicional no es verdadero, ejecutamos else
	print('El navegador que buscas no está en la lista.')##imprimimos resultados
