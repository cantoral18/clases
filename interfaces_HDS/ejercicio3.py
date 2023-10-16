
from tkinter import*
ventana=Tk()
ventana.geometry("400x500")

Widget_uno=Frame()
Widget_uno.grid(row=0,column=0)
Widget_uno.config(width=400,height=50)

etiqueta=Label(ventana,text="nombre y apellido ")
etiqueta.grid(row=0,column=0, )


cuadro_texto=Entry()
cuadro_texto.grid(row=0,column=1)
cuadro_texto.pack(anchor="se")





ventana.mainloop()