#primero importar la libreria
from tkinter import*
#instanciamos nuestra clase tk()
ventana=Tk()#clase para crear una ventana
ventana.title("clase radiobutton")#haciendo el uso de metodo title para el titulo de mi ventana
ventana.geometry("400x300")#haciendo el uso del metodo geometry para asignarle el tamaño de mi ventana


#~instanciarmi clase label

etiqueta=Label(ventana,text="radio buttons")#clase para crear etiqueta
#identificar la parte de mi ventana que deseo que muestre
#puedo usar el metodo grid o pack

etiqueta.config(fg="red",font=50)
etiqueta.pack()

info=IntVar()
def mostrar_radio():
    # respuesta="eres masculino"if info.get()==1 else"eres femenino"
    # etiquetaRespuesta=Label(ventana,text=respuesta)
    # etiquetaRespuesta.pack()
    if info.get()==1:
        etiquetaRespuesta=Label(ventana,text="eres masculino")
        etiquetaRespuesta.pack()
    else:
        etiquetaRespuesta=Label(ventana,text="eres femenino")
        etiquetaRespuesta.pack()


  
#instanciar la clase radiobutton

radiomasculino=Radiobutton(ventana,text="masculino",value=1,variable=info)
radiomasculino.pack()
radiofemenino=Radiobutton(ventana,text="femenino",value=0,variable=info)
radiofemenino.pack()
#instanciar la clase button
boton=Button(ventana,text="enviar",command=mostrar_radio)
boton.pack()

#llamar el metodo de tk que me permite tener presistencia al mostrar la ventana
ventana.mainloop()