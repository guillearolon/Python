#Se crea un txt:
f = open('fichero.txt', 'w')
f.write("Esto es una prueba")

f.close()

#agregar una linea al txt:
f = open('fichero.txt', 'a')
f.write("\n una nueva linea")

f.close()

#leer el txt:
f = open('fichero.txt', 'r')
leer = f.read()
print(leer)

f.close()