from tkinter import*
from tkinter.messagebox import *
def f_limpiar (ventana):
    ventana.nombre_texto.delete(0,END)
    ventana.apellidos_texto.delete(0,END)
    ventana.celular_texto.delete(0,END)
    
    ventana.nombre_texto.focus()

def f_nuevo(ventana):
    nombre=ventana.nombre_texto.get() 
    apellidos=ventana.apellidos_texto.get()
    celular=ventana.celular_texto.get() 
    showinfo(title="Nuevo",message="nuevo contacto agregado")
    
    ventana.tabla_datos.insert("",END,text=nombre,values=(apellidos,celular)) 
    f_limpiar(ventana)
    
def f_eliminar(ventana):
    elem_eliminar=ventana.tabla_datos.selection()
    ventana.tabla_datos.delete(elem_eliminar)
    showwarning(title="ELIMINAR",message="REGISTRO ELIMINADO")
    
def f_actualizar(ventana):
    if ventana.nombre.texto.get()=="":
        print("no hay nada")
        showerror(title="SIN DATOS",message="NO HAY NADA PARA ACTUALIZAR")
    else:    
        nombre=ventana.nombre_texto.get() 
        apellidos=ventana.apellidos_texto.get()
        celular=ventana.celular_texto.get()
        elem_actualizar=ventana.tabla_datos.selection()
        mensaje=askyesno(title="ACTUALIZAR",message="ESTAS SEGURO QUE DESEAS ACTUALIZAR")
        if mensaje == True:
            f_limpiar(ventana)
            ventana.tabla_datos.selection_remove(elem_actualizar)
            return ventana.tabla_datos.item(elem_actualizar,text=nombre,values=(apellidos,celular))
        else:
            showinfo(title="NO ACTUALIZO"message="NO SE ACTUALIZO NINGUN REGISTRO")
            f_limpiar(ventana)
            ventana.tabla_datos.selection_remove(elem_actualizar)
            

def f_dobleClick(ventana,event):
    elem_actualizar=ventana.tabla_datos.selection()
    captura_datos=ventana.tabla_datos.item(elem_actualizar)
    mensaje=askyesnocancel(title="ACTUALIZAR",message="DESEA ACTUALIZAR LOS DATOS")
    if mensaje == True:
        nombre=captura_datos["text"]
        apellidos=captura_datos["values"][0]
        celular=captura_datos["evalues"][1]
        ventana.nombre_texto.insert(0,nombre)
        ventana.apellidos_texto.insert(0,apellidos)
        ventana.celular_texto.insert(0,celular)
        ventana.tabla_datos.selection_remove(elem_actualizar)
        
    else:
        showinfo(title="ACTUALIZAR",message="NINGUN REGISTRO SELECCIONADO PARA ACTUALIZACION")
 

    


    