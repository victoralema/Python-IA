##21310193 Victor Eduardo Aleman Padilla
##usaremos clases metodo init
class CiberTlacuaches:##Creamos clase con todo y sus atributos
    def __init__(self, nombre,arma,poderespecial):##Creamos objetos con los siguientes datos
        self.nombre=nombre##Guardamos el nombre
        self.arma=arma##Guardamos su arma
        self.poderespecial=poderespecial##Guardamos poder
    def Informe(self):##Metodo
        print('El super Tlacuache ',self.nombre,' lleva un',self.arma,'y tiene el super poder ',self.poderespecial)##imprimimos datos de mi clase
class Sniper(CiberTlacuaches):##se crea una clase hija
    pasiva='lethal tempo'##atributo de la clase hija
    def passv(self):##metodo 
        print('Su pasiva es: ',self.pasiva,' ralentiza el tiempo cuando un golpe es letal\n')##imprimimos los datos de la clase
class Berserk(CiberTlacuaches):##Creamos clase hija
    pasiva='Inquebrantable'##Atributos de la clase hija
    def passv(self):##Metodo
        print('Su pasiva es: ',self.pasiva, ' No sufre retroceso cuando le queda poca vida\n')##Imprimimos datos de la clase
ct1=Sniper('Mimoso',' Rompedor de taquiones','Autocuracion')##Creamos objeto y le asignamos atributos
ct1.Informe()##LLamamos metodo
ct1.passv()##Llamamos metodo
ct1.poderespecial='Supercuracion'##Cambiamos el valor de la variable
print("Mejoramos tu superpoder ahora es: ",ct1.poderespecial)##imprimimos el cambio
ct2=Berserk('Peluchín',' Fierro Golpeador de Parejas Felices','Antidebilatacion')##Creamos objetos y asignamos atributos
ct2.Informe()##llamamos metodo
ct2.passv()##llamamos metodo
ct2.arma='a Mano'##cambiamos el valor del atributo
print('Te quitaron tu arma ahora tus stats son: ')##Mostramos la modificacion
ct2.Informe()##llamamos metodo
ct2.passv()##llamamos metodo
del ct2##Borramos objeto
