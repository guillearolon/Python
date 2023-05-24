while True:
    
    capacidad_camion = int(input("Ingrese la capacidad del camión en kilogramos: "))
    
    peso_actual = 0
    
    while True:
        
        if peso_actual > capacidad_camion:
            print("El camión está lleno. Debe despacharlo y comenzar a cargar otro.")
            break
        
        peso_saca = int(input("Ingrese el peso de la saca en kilogramos: "))
        
        peso_actual += peso_saca
        
        if peso_actual == capacidad_camion:
            print(f"El camión está listo para partir con {peso_actual} kilogramos.")	
            break
        
        continuar = input("¿Desea cargar otra saca? (Sí/No): ")
        
        if continuar.lower() == "no":
            break
        
    
    continuar_carga = input("desea cargar otro camion? (Si/No): ")
        
    if continuar_carga.lower() == "no":
        break
        
    else:
        continue