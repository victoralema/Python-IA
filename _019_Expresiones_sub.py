##21310193 Victor Eduardo Aleman Padilla
import re##importamos cadena de caracteres

texto = "tres tristes tigres comen trigo en un trigal"##creamos varibale y le asignamos un valor (texto)
busqueda = re.sub(" ",  "-",  texto)##buscamos en el texto y por cada espacio, reemplazamos por un "-"
print(busqueda)##imprimimos varibale
