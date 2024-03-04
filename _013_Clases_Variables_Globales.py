##21310193 Victor Eduardo Aleman Padilla
##Clases y variables globales
def vacio():##Creamos funcion sin parametros ni retorno
    global numero1##Creamos variable global
    numero1=75##Le damos un valor
def nido():##creamos clase 
    vacio()##llamamos funcion vacio dentro de la clase
    numero2=43##creamos y asignamos valor a la variable
    numero2=numero1+numero2##Sumamos nuestras varibales de vacio y nido y guardamos en varibale del nido
    print('El resultado es: ',numero2)##Imprimimos resultado
nido()##LLamamos a la funcion
