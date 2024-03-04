##21310193 Victor Eduardo Aleman Padilla
##Buscaremos expresiones regulares y usaremos el findall
import re##Importamos cadena de caracteres

texto = "tres tristes tigres comen trigo en un trigal"##Almacenamos un texto en nuestra variable texto
busqueda = re.findall("es", texto)##Busca todas las terminaciones en "es" que hay en el texto y las guarda en la cadena busqueda
print(busqueda)##Imprime busqueda
