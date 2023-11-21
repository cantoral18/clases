import datetime
COLOR_DE_FONDO_PRIMARIO ="#ccccff"
COLOR_FONDO_SECUNDARIO="#b3daff"  
TITULO_APP="App de contactos"

date=datetime.datetime.now()
HORA_ACTUAL=f"{date.day}-{date.month}-{date.year},hora:{date.hour}:{date.minute}"

def centrar_ventana(ventana,ancho_ventana,largo_ventana):
    pantalla_ancho=ventana. winfo_screenwidt()
    pantalla_largo=ventana. winfo_screenheigt()
    x=int((pantalla_ancho/2)-(ancho_ventana/2))
    y=int((pantalla_largo/2)-(largo_ventana))
    return ventana.geometry(f"{ancho_ventana}x{largo_ventana}+{x}+{y}")