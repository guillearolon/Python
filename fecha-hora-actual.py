#Imprimir fecha y hora actual con libreria "datetime":

import datetime 

fecha_actual = datetime.datetime.now() #por defecto
fecha_formateada = fecha_actual.strftime("%d/%m/%Y %H:%M:%S") #le damos formato

print(f"La hora y fecha actual es: {fecha_formateada}")