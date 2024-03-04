##21310193 Victor Eduardo Aleman Padilla
##expresiones regulares
import re##importamos la funcion de expresiones
texto = "Bienvenidos a Programación fácil"##Guardamos texto en nuestra variable texto
busqueda = re.search("Bienvenidos", texto)##buscamos con la funcion search una coincidencia en la cadena re y lo conservamos en busqueda
print(busqueda)##imprimimos busqueda
