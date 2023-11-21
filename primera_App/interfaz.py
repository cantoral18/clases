from tkinter import *
from config import *

class InterfazApp(Tk):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.construir_widget
#metodo propio vamos adarle las configuraciones basicas 
# para mostrar nuestra ventana
def configurar_ventana(self):
    self.title(f"{TITULO_APP} {HORA_ACTUAL}")
    self.configure(bg=COLOR_DE_FONDO_PRIMARIO)
    self.resizable(0,0)
    self.attributes("-alpha", 0.96)
    w,h=870,470
    centrar_ventana(self,w,h)
    
def contruir_widget(self):
    #CAJITAS DE TEXTO
    self.cajas_texto=LabelFrame(self,text="cajas de texto",width=150,height=430,
                                relief=FLAT ,bg=COLOR_DE_FONDO_PRIMARIO,fg="white",font=("arial",12))
    self.cajas_texto.grid(row=0,column=0,padx=20,pady=20)
    self.label_nombre=Label(self.cajas_texto,text="nombres",bg=COLOR_DE_FONDO_PRIMARIO,fg="white",font=("Roboto",10)).pack(pady=10)
    #FIN CAJITA DE TEXTOS

    
    
