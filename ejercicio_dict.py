'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.'''

nombre = input("¿Cuál es su nombre? ")
edad = int(input("¿Cual es su edad? "))
direccion = input("¿Cuál es su dirección? ")
telefono = int(input("Introducir su numero telefonico: "))


dic = {'Nombre':nombre.title(), 'Edad':edad, 'Dirección':direccion.title(), 'Telefono':telefono}

print(dic['Nombre'],"tiene",dic['Edad'],"años","vive en",dic["Dirección"],"y su numero de telefono es",dic["Telefono"])
