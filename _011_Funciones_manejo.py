##21310193 Victor Eduardo Aleman Padilla
##Usaremos funciones argumentos diccionarios arbitrario
def Vacio ():##Creamos funcion de manejo
    print('Esta funcion tiene hambre')#Imprimimos 
    valor=1##creamos una variable con el valor de 1
    return valor##
def Tupla(*args):##Guardamos dinamicamente los argumentos en forma de tupla
    print('Los datos que tengo son: ',args)#imprimimos argumentos de tupla
    
def Diccionario(**kwargs):##Creamos funcion que guarde en forma de diccionario
    print('Los datos que tengo son: ',kwargs)##imprimimos argumentos
def Paquetaxo(*args,**kwargs):##guardamos de dos formas los argumentos de forma dinamica
    print(args)##imprimimos argumentos
    print(kwargs)##imprimimos argumentos*kwargs
x=Vacio()##pedimos funcion vacio y guardamos en variable x
Tupla('Fernando','Agustin','Idelfonso','Leonardo')##Guardamos argumentos en forma de string
Diccionario(animal1='Capibara',animal_2='Pejelagarto',animal_3='Huajolote')##guardamos argumentos en forma de diccionario
Paquetaxo("Yo",'Soy,',argumento1='Dios')###Enviamos los dos tipos de argumentos
if(x==1):##comparamos los datos en x
    print('Hasta luego')##Enviamos un texto de despedida para el final
