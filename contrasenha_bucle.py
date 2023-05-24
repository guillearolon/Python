'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''

contrasenha = "Nueva123"
intentos = 1 #inicio en 1 hasta llegar a 3 intentos, si la contraseña no coincide.

while intentos <= 3:
    ingreso = input("Ingrese contraseña: ")
    if ingreso == contrasenha:
        print("¡Contraseña correcta!")
        break
        
    else:
        print(f"Contraseña incorrecta, van {intentos} intentos.")
        intentos=intentos+1
        
    print("Usted superó los tres intentos")            
    