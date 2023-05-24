'''Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.'''

lista_vacia = []

contador = 1 #inicia el contador en 1

while contador <= 5: #mientras sea menor o igual 5 ejecutar:
    numeros_ganadores = int(input("Introduce los numeros ganadores: "))
    contador=contador+1
    lista_vacia.append(numeros_ganadores) #agrego los numeros ingresador a la lista vacia.
    lista_vacia.sort() #los ordeno de menor a mayor
    

    
print(f"Los numeros ganadores son: {lista_vacia}")