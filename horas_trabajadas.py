'''Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.'''

horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
coste_x_horas = int(input("ingrese el coste por hora: "))

paga_correspondiente = horas_trabajadas * coste_x_horas

print(f"La paga correspondiente es ${paga_correspondiente}")
                      
                      