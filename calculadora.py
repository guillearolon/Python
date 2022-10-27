from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

i = 0

#entrada de texto:
e_texto = Entry(ventana, font= ("Calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

#funciones:
def click (valor):
    global i
    e_texto.insert(i, valor)
    i+= 1

def borrar ():
    e_texto.delete(0, END)
    i = 0
    
def operaciones ():
    operacion = e_texto.get() #lo que se inserte en el cuadro, luego se evalua.
    resultado = eval(operacion)
    e_texto.delete(0, END) #aqui se borra la operacion y luego se muestra el resultado en limpio
    e_texto.insert(0, resultado)
    
#botones:
boton_1 = Button(ventana, text= "1", width = 5, height = 2, command = lambda: click(1))
boton_2 = Button(ventana, text= "2", width = 5, height = 2, command = lambda: click(2))
boton_3 = Button(ventana, text= "3", width = 5, height = 2, command = lambda: click(3))
boton_4 = Button(ventana, text= "4", width = 5, height = 2, command = lambda: click(4))
boton_5 = Button(ventana, text= "5", width = 5, height = 2, command = lambda: click(5))
boton_6 = Button(ventana, text= "6", width = 5, height = 2, command = lambda: click(6))
boton_7 = Button(ventana, text= "7", width = 5, height = 2, command = lambda: click(7))
boton_8 = Button(ventana, text= "8", width = 5, height = 2, command = lambda: click(8))
boton_9 = Button(ventana, text= "9", width = 5, height = 2, command = lambda: click(9))
boton_0 = Button(ventana, text= "0", width = 13, height = 2, command = lambda: click(0))

#botones simbolos:
boton_borrar = Button(ventana, text= "AC", width = 5, height = 2, command = lambda: borrar())
boton_parentesis1 = Button(ventana, text= "(", width = 5, height = 2, command = lambda: click("("))
boton_parentesis2 = Button(ventana, text= ")", width = 5, height = 2, command = lambda: click(")"))
boton_punto = Button(ventana, text= ".", width = 5, height = 2, command = lambda: click("."))

#botones operaciones:
boton_div = Button(ventana, text= "/", width = 5, height = 2, command = lambda: click("/"))
boton_mult = Button(ventana, text= "*", width = 5, height = 2, command = lambda: click("*"))
boton_sum = Button(ventana, text= "+", width = 5, height = 2, command = lambda: click("+"))
boton_rest = Button(ventana, text= "-", width = 5, height = 2, command = lambda: click("-"))
boton_igual = Button(ventana, text= "=", width = 5, height = 2, command = lambda: operaciones()) #asiganamos la fun "operaciones"

#agregar estos botones en pantalla:
boton_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_div.grid(row = 1, column = 3, padx = 5, pady = 5)

boton_7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton_8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton_9.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_mult.grid(row = 2, column = 3, padx = 5, pady = 5)

boton_4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton_5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton_6.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_sum.grid(row = 3, column = 3, padx = 5, pady = 5)

boton_1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton_2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton_3.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_rest.grid(row = 4, column = 3, padx = 5, pady = 5)

boton_0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
boton_punto.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 5, column = 3, padx = 5, pady = 5)



ventana.mainloop()