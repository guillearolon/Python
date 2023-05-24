'''Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.'''

palabra = input("Ingrese una palabra: ")

contador = 1

while contador <= 10:
    print(f"{contador} = {palabra}")
    contador=contador + 1