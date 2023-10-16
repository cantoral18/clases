# import tkinter -> libreria para la creacion de interfaces graficas
#otro metodo
# import tkinter as tk
# root =tk.tk()
# mas rapido
from tkinter import *

#la libreria tkinter tiene tres grandes clases para la creacion de interfaces
# la mas conocidas  es tk()
# tkk()
# tcl()
#2 . instanciar tk() como generador de interfaz grafica
nueva_ventana=Tk()

# 3. Frame es tambien una clase Frame()para crear un Frame tengo que instanciarlo
#crea la ventana
menu_principal=Frame()
#montamos o inicializamos el frame
menu_principal.pack()
# haciendo el uso del metodo config le damos el tamaño
menu_principal.config(width="200",height="200")
# haciendo uso del metodo config le asignamos un color
menu_principal.config(bg="pink")

# metodo tk() que mantiene la ejecucuion del programa en un bucle
nueva_ventana.mainloop()

