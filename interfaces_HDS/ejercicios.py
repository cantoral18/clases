from tkinter import *
ventana=Tk()

widget_uno=Frame()

widget_uno.grid(row="0",column="0")
widget_uno.config(width="300",height="300")
widget_uno.config(bg="pink")

widget_dos=Frame()
widget_dos.grid(row="0",column="1")
widget_dos.config(width="300",height="300")
widget_dos.config(bg="black")

widget_tres=Frame()
widget_tres.grid(row="1",column="0")
widget_tres.config(width="600",height="300")
widget_tres.config(bg="violet")

widget_cuatro=Frame()
widget_cuatro.grid(row="500",column="0")
widget_cuatro.config(width="300",height="300")
widget_cuatro.config(bg="sky blue")


widget_cinco=Frame()
widget_cinco.grid(row="700",column="0")
widget_cinco.config(width="300",height="300")
widget_cinco.config(bg="yellow")





ventana.mainloop()
