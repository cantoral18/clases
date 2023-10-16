
from tkinter import*

# instanciar la clase
ventana=Tk()
ventana.geometry("400x500")
# creacion mis dos widget de orden inferior con la clase Frame()
Widget_uno=Frame()
Widget_uno.grid(row=0,column=0)
Widget_uno.config(width=400,height=50)


# creacion de etiquetas
etiqueta=Label(ventana,text="ingrese su nombre :) ")
etiqueta.grid(row=0,column=0)
# creacion de cuadros de texto
cuadro_texto=Entry()
cuadro_texto.grid(row=2,column=0)


# usar el metodo lopp para que la ventana permanesca abieta
ventana.mainloop()

