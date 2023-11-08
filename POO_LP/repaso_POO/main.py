# from rich import print
# from rich,Markdown import Markdown
# #titulo
# edad=20
# respuesta="es mayor" if edad<17 else " es menor de edad"
# texto="""
# #parrafo
# ```bash
# git commit -m"titulo"  -m "cuerpo del commit"
# #comentario
# ```
# *lista
# *lista
# >informacion valiosa
# ()



# """,format(respuesta)

# mostrar_mark=Markdown(texto)
# print(mostrar_mark)


#repaso de programacion orientada a objetos
class Mascota:
    
   def __init__(self):
       self.nombre=None 
       self.edad=None
       self.tipo_animal=None
   def hablar(self,sonido):
        return sonido
    def datos_mascota(self,nombre,edad,tipo_animal):
        self.nombre=nombre
        self.edad=edad
        self.tipo_animal=tipo_animal
    
    
#repaso de programacion orientada a objetos
class Perro(Mascota):
    def atacar(self):
        return "ladra y muerde"      
class Gato(Mascota):
    pass

perro_boby=Perro()
perro_boby.datos_mascota("boby",14,"perro")  
print(f"[bold blue]"+perro_boby.hablar('gua..'))
print("[bold blue]"+perro_boby.atacar())
print("[bold blue]"+perro_boby.nombre+" "+perro_boby.tipo_animal)


class Persona:
    
   def __init__(sel, nombre:str,edad:int,sexo:str):
       self.nombre=nombre
       self.edad=edad
       self.sexo=sexo
    def comen(self,plato_favorito:str):
        return f"yo{self.nombre}estoy comiendo mi{plato_favorito}"
    def cagan(self):
        return "pipi" 
    
    
class Estudiante(Persona):
    def _init__(sel, nombre:str,edad:int,sexo:str,carrera_profesional:str):
       super().__init__(nombre,edad,sexo)
       self.carrera_profesional=carrera_profesional
    def estudiar(self
        return "estoy estudiando")
    
class trabajar(Persona):
    def _init__(sel, nombre:str,edad:int,sexo:str,cprofesion:str):
       super().__init__(nombre,edad,sexo)
       self.profesion=profesion
    def trabajar(self
        return "estoy trabajndo")
    
    
    
    
    
    
    
   