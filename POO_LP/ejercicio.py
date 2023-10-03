#1. haciendo uso de POO crear un objeto para entidad celular
# class celular:
#     marca="lg"
#     año="2023 años"
#     color="negro"
    
    
#     def encender (self):
#         return "encendido"
#     def apagar(self,apagando):
#         blanco=f"apagar{apagando},apagando"
#         return "blanco"

# respuesta =celular
# print(respuesta . encender)
# print(respuesta . apagar)

# 2.haciendo uso de POO crear un objeto para entidad vehiculo
  

# class Vehiculo:
def __init__(self, marca, modelo, año, numero_serie):
         self.marca = marca
         self.modelo = modelo
         self.año = año
         self.numero_serie = numero_serie
def obtener_informacion(self):
         return f"Vehículo: {self.marca} {self.modelo}, Año: {self.año}, Número de Serie: {self.numero_serie}"


mi_vehiculo = Vehiculo("Toyota", "Corolla", 2023, "1869574")

print(mi_vehiculo.obtener_informacion())



# 3. haciendo uso de POO crear un objeto para entidad avion

# class Avion:
    
#     marca ="JHOSI"
#     modelo = ""
#     año = 1999
#     numero_serie = 145863

   
#     def volar(self):
#         return "vuelo "
#     def aterrizar(self,hora):
#         aterrizando=f"aterrizar{hora},hora"
#         return " aterrizando"


# respuesta =Avion
# print(respuesta.marca)
# print(respuesta . aterrizar)



#4. haciendo uso de POO crear un objeto para entidad dota2

# class Dota2:
    
#     nombre ="dota2"
#     año = 2023
#     color="blanco y negro"

   
#     def ganas(self):
#         return "ganaste"
#     def pierdes(self):
#         pierdes=f"pierdes"
#         return "pierdes"


# respuesta =Dota2
# print(respuesta.nombre)
# print(respuesta.ganas)



# 5.haciendo uso de POO crear un objeto para una pc

# class Pc:
    
#     marca ="lg"
#     modelo = "actual"
#     año = 2019
#     color="negro"

   
#     def prende(self):
#         return "prendido"
#     def busca_informacion(self,hora):
#         informa=f"busca_informacion{hora},hora"
#         return "buscando_informacion"


# respuesta =Pc
# print(respuesta.marca)
# print(respuesta . busca_informacion)


# 6 . haciendo uso de POO crear un objeto para entidad impresora

# class Impresora:
    
#     marca ="lg"
#     modelo = "actual"
#     año = 2023
#     color="blanco"

   
#     def prende(self):
#         return "prendido"
#     def imprimiendo(self,hora):
#         imprime=f"imprimiendo{hora},hora"
#         return "imprimiendo"


# respuesta =Impresora
# print(respuesta.marca)
# print(respuesta.año)
# print(respuesta.imprimiendo)


# 7.haciendo uso de POO crear un objeto para emitir una factura
class Factura:
    cliente_nombre="tony"
    num_factura="2"
   
    
    def total_compra(self):
        return "total_compra"
    def precio_articulos(self,precio):
        p=f"precio_articulos{precio},precio"
        return "precio_articulo "


respuesta =Factura
print(respuesta.cliente_nombre)
print(respuesta .total_compra)