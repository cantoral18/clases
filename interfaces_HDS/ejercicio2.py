# jercicio 2

from tkinter import *
ventana=Tk()

widget_uno=Frame()
widget_uno.grid(row="0",column="0",rowspan="1")
widget_uno.config(width="100",height="200")
widget_uno.config(bg="pink")

widget_dos=Frame()
widget_dos.grid(row="0",column="1",rowspan=1,columnspan=1)
widget_dos.config(width="100",height="100")
widget_dos.config(bg="black")

widget_tres=Frame()
widget_tres.grid(row="1",column="1")
widget_tres.config(width="100",height="100")
widget_tres.config(bg="yellow")

widget_cuatro=Frame()
widget_cuatro.grid(row="2",column="0",rowspan=1,columnspan=2)
widget_cuatro.config(width="200",height="100")
widget_cuatro.config(bg="violet")





ventana.mainloop()
