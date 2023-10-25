##1. EJEMPLO
# from tkinter import*
# ventana=Tk()
# ventana.title("mi ventana ♥ ")
# ventana.geometry("500x400")

# colum_izquierda=Frame()
# colum_izquierda.grid(row=0,column=0)
# colum_izquierda.config(width=200,height=5)
# etiqueta=Label(ventana,text="esta es mi etiqueta")
# etiqueta.grid(row=0,column=1)

# ventana.mainloop()



from tkinter import*
ventana=Tk()
ventana.title("mi ventana ♥ ")
ventana.geometry("500x400")

header=Frame()
header.grid(row=0,column=0,columnspan=4)
header.config(width=500,height=15,bg="violet")

aside=left=()
aside.grid(row=1,column=0,rowspan=7)
aside.config(width=15,height=385,bg="violet")

etiqueta_usuario=label


ventana.mainloop()

