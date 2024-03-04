##21310193 Victor Eduardo Aleman Padilla
##usaremos la funcion strftime
import datetime##importamos datatime

ahora = datetime.datetime.now()##Creamos varibale para guardar nuestra fecha

print(ahora.strftime("Día de la semana abreviado: %a "))##Imprimimos semana
print(ahora.strftime("Día de la semana completo: %A "))##imprimimos dia de la semana
print(ahora.strftime("Mes abreviado: %b "))##imprimimos mes
print(ahora.strftime("Mes abreviado: %B "))##imprimimos el mes abreviado
print(ahora.strftime("Fecha completa: %c "))##imprimimos fecha completa
print(ahora.strftime("Siglo (empieza a contar desde cero): %C "))##siglo actula
print(ahora.strftime("Día del mes (01 - 31): %d "))##dia del mes
print(ahora.strftime("Día/hora/año: %D "))##hora año y dia
print(ahora.strftime("Día del mes (1 - 31): %e "))##dia del mes
print(ahora.strftime("Año en dos dígitos: %g "))##año en digitos
print(ahora.strftime("Año en cuatro dígitos: %G "))##imprimimos año con cuatro digitos
print(ahora.strftime("Mes abreviado: %h "))##imprimimos mes abreviado
print(ahora.strftime("Hora (00 - 23): %H "))##imprimimos hora en formato 24
print(ahora.strftime("Hora (01 - 12): %I "))##imprimimos en formato de 12
print(ahora.strftime("Día del año: %j "))##imprimimos dia del año
print(ahora.strftime("Mes del 01 al 12: %m "))##imprimimos mes en digito
print(ahora.strftime("Minuto: %M "))##imprimimos minuto vivido
print(ahora.strftime("Salto de línea: %n"))##imprimimos salto de linea
print(ahora.strftime("AM o PM: %p "))##imprimimos mañana o tarde
print(ahora.strftime("Hora + AM o PM: %r"))##imprimimos hora con formato de mañana o tarde
print(ahora.strftime("Hora y minutos: %R"))##imprimimos hora con minutos
print(ahora.strftime("Segundos: %S"))##imprimimos segundos corriendo
print(ahora.strftime("Tabulación: %t"))##imprimimos la tabulacion
print(ahora.strftime("Hora, minutos y segundos: %T"))##imprimimos hora minuto y segundo
print(ahora.strftime("Día de la semana (número): %u"))##imprimimos dia de la semana con numero
print(ahora.strftime("Semana del año (empieza en domingo): %U"))##imprimimos semana del año
print(ahora.strftime("Semana del año(Condiciones especiales): %V"))##imprimimos semana del año
print(ahora.strftime("Semana del año (empieza en lunes): %W"))##imprimimos dia de la semana
print(ahora.strftime("Día de la semana (empieza en domingo): %w"))##imprimimosdia de la semana
print(ahora.strftime("Día/mes/año de dos dígitos: %x"))##imprimimos dia mes año
print(ahora.strftime("Hora/minutos/segundos: %X"))##imprimimos hora minutos segundos
print(ahora.strftime("Año corto: %y"))##imprimimos año normal
print(ahora.strftime("Año largo: %Y"))##imprimimos año bisiesto
