'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.'''

contrasenha = "Nueva123"

usuario = input("Ingrese la contraseña: ")

if usuario == contrasenha:
    print("Es correcta, puede ingresar")
    
else:
    print("Contraseña incorrecta")
    
        