from tkinter import*
def enviar_boton(ventana,valor):
   if valor == "=":
       print("soy igual")
   elif valor=="C":
       ventana.caja_operaciones_label.config(text="FSD")
       ventana.operacion_label.delete(0,END)
       
   elif valor=="<":
       valor_actual=ventana.caja_operaciones.get()
       if valor_actual:
           nuevo_valor=valor_actual[1-1]
           ventana.caja_operaciones.delete(0,END)
       
   else:
       print(f"soy el valor(valor)")
       
       
def cambio_tema(ventana,colores):
        if ventana.tema_oscuro:
            ventana.configure(dg=colores.color_fondo_ligth)
            ventana.caja_operaciones.config(fg=colores.color_texto_ligt,bg= colores.color_caja_texto_ligth)
            ventana.operacion_label.config(fg=colores.color_texto_light,bg=colores.color_fondo_light)
            ventana.boton_tema.configure(text="/uf185 modo claro",relief=sunken,bg=color.color_botiones_especial_light)
    else:
            ventana.configure(dg=colores.color_fondo_negro)
            ventana.caja_operaciones.config(fg=colores.color_texto_negro,bg= colores.color_caja_texto_negro)
            ventana.operacion_label.config(fg=colores.color_texto_negro,bg=colores.color_fondo_negro)
            ventana.boton_tema.configure(text="/uf185 modo oscuro",relief=sunken,bg=color.color_botiones_especial_negro)
        ventana.tema_oscuro=not ventana. tema_oscuro