## Para mostrar el texto “¡Hola mundo!” en una ventana:
from tkinter import Label, Tk

apl = Tk()
texto = Label(apl, text="¡Hola mundo!")
texto.pack()
apl.mainloop()