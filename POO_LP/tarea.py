#  tarea 
#  crear una lista con 10 objetos que contengan los datos de las tiendas comerciales
# ejemplo:
#      ```python
#     tiendas=[
#         {
#             "ruc":96325841
#             "nombre":"carlos",
#             "categoria":["abarrotes","bodega"],
#             "horario_atencion":{
#                 "dia":7am-12m,
#                 "tarde":2pm-8pm
#             }
#             "gerente":"manuel"

#         }
#      ]
#      ```

#      ### observacion : las categorias sera:4 abarrotes, farmacia,bodega,restaurante
#      ###observacion: los gerente solo podran ser los siguientes :
#      ale,luis,mary,jhosi

#      ##realizae los siguientes ejercicios
#      ##crear una clase para tiendas que tenga los siguientes metodos o caso de uso
#      1. crear un metodo que me filtre las tiendas que tienen cada gerente
#      2. crear un metodo que me muestre los negocios que tiene  mas de dos categorias
#      3. crear un metodo que me muestre solo el nombre y ruc de los tiendas


#      print(llamandoJori.familia)
# print(llamandoNadine.llamar("ollanta")) -->




class Tienda:
    def __init__(self, ruc, nombre, categorias, horario_atencion, gerente):
        self.ruc = ruc
        self.nombre = nombre
        self.categorias = categorias
        self.horario_atencion = horario_atencion
        self.gerente = gerente

    def __str__(self):
        return f"Nombre: {self.nombre}, RUC: {self.ruc}"

class ListaTiendas:
    def __init__(self):
        self.tiendas = []

    def agregar_tienda(self, tienda):
        self.tiendas.append(tienda)

    def filtrar_por_gerente(self, gerente):
        return [tienda for tienda in self.tiendas if tienda.gerente == gerente]

    def negocios_mas_de_dos_categorias(self):
        return [tienda for tienda in self.tiendas if len(tienda.categorias) > 2]

    def mostrar_nombre_y_ruc(self):
        return [(tienda.nombre, tienda.ruc) for tienda in self.tiendas]


tiendas = ListaTiendas()

tienda1 = Tienda(96325841, "Carlos", ["abarrotes", "bodega"], {"dia": "7am-12m", "tarde": "2pm-8pm"}, "manuel")
tienda2 = Tienda(12345678, "Tienda1", ["abarrotes", "farmacia"], {"dia": "8am-1pm", "tarde": "2pm-8pm"}, "ale")
tienda3 = Tienda(87654321, "Tienda2", ["restaurante"], {"dia": "9am-2pm", "tarde": "2pm-8pm"}, "ale")
tienda4 = Tienda(13579246, "Tienda3", ["bodega"], {"dia": "7am-12m", "tarde": "2pm-8pm"}, "mary")
tienda5 = Tienda(98765432, "Tienda4", ["abarrotes", "bodega", "farmacia"], {"dia": "10am-3pm", "tarde": "2pm-8pm"}, "jhosi")

tiendas.agregar_tienda(tienda1)
tiendas.agregar_tienda(tienda2)
tiendas.agregar_tienda(tienda3)
tiendas.agregar_tienda(tienda4)
tiendas.agregar_tienda(tienda5)


print("Tiendas de ale:")
for tienda in tiendas.filtrar_por_gerente("jhosi"):
    print(tienda)

print("Tiendas con más de dos categorías:")
for tienda in tiendas.negocios_mas_de_dos_categorias():
    print(tienda)


print("Nombre y RUC de las tiendas:")
for nombre, ruc in tiendas.mostrar_nombre_y_ruc():
    print(f"Nombre: {nombre}, RUC: {ruc}")
    
    
