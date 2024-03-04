##21310193 Victor Eduardo Aleman Padilla
##Se pondra en uso las listas y posicion negativa
Lista = ['Celular','Zapatos','Laptop','Cadena','Cable','Ropa']##Creamos nuestra lista con 6 objetos en un array
print("Se imprimiran de la siguiente lista el dato 5 y el dato -4\n")##Imprimimos informacion para el usuario
print(Lista)##imprimimos lista
print("\nEsto es lo que contenia el dato 5:\n",Lista[5])##Imprimimos el dato guardado en la posicion 5 de nuestra lista
print("\nEsto es lo que contenia el dato -4:\n",Lista[-4])##Imprimimos el dato guardado en la posicion -4 de nuestra lista
del Lista[4]##Borramos el dato en posicion -4 de la lista
print("\nBorraremos el que este en la posicion 4: \n",Lista,"\n")##imprimimos instruccion
Lista.remove('Zapatos')##Eliminamos de la lista el dato en posicion 4
print("\nBorraremos el que diga 'Zapatos': \n",Lista,"\n")##imprimimos instruccion y la lista
print("\nAhora borraremos de la lista la posicion 0 y 2 y la guardaremos en otra lista\n")##imprimimos instruccion
Lista1 = Lista.pop(0)##Guardamos el dato eliminado en posicion 0 de la lista
Lista2 = Lista.pop(2)##Guardamos el dato eliminado en posicion 2 de la lista
lista_save=[Lista1,Lista2]##Guardamos nustros datos eliminados en un arreglo
print(Lista)##imprimimos lista
print("\nElementos guardados en la nueva lista\n")##imprimimos instruccion
print(lista_save)##imprimimos los datos removidos y guardados de la lista
print("\nAñadiremos los siguiente elementos a la lista: 'Tela' y 'Bici'\n")##imprimimos instruccion
Lista.append('Tela')##Añadimos elemento a la lista
Lista.append('Bici')##Añadimos elemento a la lista
print(Lista)##imprimimos lista
print("\nAñadiremos 'Silla' y 'Sofa' a la posicion 0 y -4\n")##imprimimos instruccion
Lista.insert(0, 'Silla')##añadimos en la posicion 0
Lista.insert(-4, 'Sofa')##añadimos en la posicion -4
print(Lista)##imprimimos lista
print("\nAcomodaremos por orden alfabetico inverso\n")##imprimimos instruccion
Lista.sort(reverse=True)##Acomodamos de manera alfabetica inversa los datos de la lista
print(Lista)##imprimimos lista
print("\nAcomodaremos por orden alfabetico\n")##imprimimos instruccion
Lista.sort(reverse=False)##Acomodamos en orden alfabetico
print(Lista)##Imprimimos lista

