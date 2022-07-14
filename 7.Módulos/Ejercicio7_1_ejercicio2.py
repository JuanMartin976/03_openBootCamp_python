# Importamos el módulo time para poder coger la hora.
import time

# Inicializamos las variables y formateamos el tiempo para que solo se vean las horas y minutos
hora = time.strftime('%H') 
minutos = time.strftime('%M') 

# Comprobamos si la hora es mayor o igual a 19. Si es mayor, mostrará un mensaje y en el caso de que sea menor mostrará un mensaje informando de las horas y minutos que faltan para ir a casa.

aCasa = 19
if int(hora) >= aCasa:
	print ("Es hora de irse a casa") 
else:
	print ("Quedan {} horas y {} minutos para irnos a casa".format((aCasa-1)- int(hora), 59-int(minutos)))
