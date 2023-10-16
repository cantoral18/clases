# importamos tkinter

from tkinter import *
# instanciar la clase tk()
ventana=Tk()
#creo mis dos widget de orden  inferior con la clase frame()


#instancio mi primer widget
widget_uno=Frame()

#usar metodo para montarel frame
widget_uno.grid(row="0",column="0")
widget_uno.config(width="100",height="100")
widget_uno.config(bg="pink")
#el metodo de grid recibe dos parametros el numero  de la columna y el numero  de la fila donde quero ubicar mi widget

# creacion de segundo widget
widget_dos=Frame()
widget_dos.grid(row="2",column="0")
widget_dos.config(width="100",height="100")
widget_dos.config(bg="yellow")



# usar el metodo  loop para la ventana permanecera abierta
ventana.mainloop()