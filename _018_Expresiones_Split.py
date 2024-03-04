##21310193 Victor Eduardo Aleman Padilla
##expresiones split
import re##importamos cadena de caracteres

texto = "tres tristes tigres comen trigo en un trigal"##creamos varibale y le asignamos un valor (texto)
busqueda = re.split("es", texto)##Buscamos en cada palabra y separamos las que terminen en es
print(busqueda)##imprimimos
