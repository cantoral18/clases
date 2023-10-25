tiendas = [
    {
        "nombre": "Tienda Uno",
        "categorias": ["abarrotes"],
        "horario_atencion": {
            "dia": "7am-12pm",
            "tarde": "2pm-8pm",
        },
        "gerente": "Edwin",
        "ruc": "1234567890"
    },
    {
        "nombre": "Farmacia Salud",
        "categorias": ["farmacia"],
        "horario_atencion": {
            "dia": "8am-1pm",
            "tarde": "3pm-9pm",
        },
        "gerente": "China",
        "ruc": "2345678901"
    },
    {
        "nombre": "Bodeguita pepe",
        "categorias": ["bodega"],
        "horario_atencion": {
            "dia": "7am-12pm",
            "tarde": "1pm-7pm",
        },
        "gerente": "Edwin",
        "ruc": "3456789012"
    },
    {
        "nombre": "Tienda de abarrotes",
        "categorias": ["abarrotes", "farmacia"],
        "horario_atencion": {
            "dia": "6am-11am",
            "tarde": "3pm-8pm",
        },
        "gerente": "Edwin",
        "ruc": "4567890123"
    },
    {
        "nombre": "Farmacia Bienestar",
        "categorias": ["farmacia"],
        "horario_atencion": {
            "dia": "9am-1pm",
            "tarde": "4pm-10pm",
        },
        "gerente": "Edwin",
        "ruc": "5678901234"
    },
    {
        "nombre": "Super Abarrotes",
        "categorias": ["abarrotes"],
        "horario_atencion": {
            "dia": "7am-12pm",
            "tarde": "2pm-9pm",
        },
        "gerente": "china",
        "ruc": "6789012345"
    },
    {
        "nombre": "Bodega de yadira",
        "categorias": ["bodega"],
        "horario_atencion": {
            "dia": "7am-12pm",
            "tarde": "1pm-7pm",
        },
        "gerente": "yadira",
        "ruc": "7890123456"
    },
    {
        "nombre": "Mini bodega",
        "categorias": ["abarrotes", "bodega"],
        "horario_atencion": {
            "dia": "6am-11am",
            "tarde": "3pm-8pm",
        },
        "gerente": "Edwin",
        "ruc": "8901234567"
    },
    {
        "nombre": "Tienda Saludable de frutas",
        "categorias": ["abarrotes", "farmacia"],
        "horario_atencion": {
            "dia": "7am-12pm",
            "tarde": "2pm-9pm",
        },
        "gerente": "Edwin",
        "ruc": "9012345678"
    },
    {
        "nombre": "Supermercado ",
        "categorias": ["abarrotes", "farmacia", "bodega"],
        "horario_atencion": {
            "dia": "8am-12pm",
            "tarde": "2pm-9pm",
        },
        "gerente": "Nadine",
        "ruc": "2345678901"
    }
]

class Tienda:

    def filtrar_por_gerente(self,tiendas, nombre_gerente):
        return list(filter(lambda el : el["gerente"] == nombre_gerente, tiendas))

    def negocios_con_mas_de_dos_categorias(self,tiendas):
        return list(filter(lambda tienda : len (tiendas) > 2, tiendas))

    def mostrar_nombre_y_ruc(self,tiendas):
        nuevo_objetos=list(map(lambda par:{"ruc":par["ruc"],"nombre":par["nombre"]},tiendas))
        return nuevo_objetos
    
    def ruc_nombre(self,bd_tiendas):
        respuesta=list(map(lambda el:{
            "nombre_gerente":el["nombre"],
            "ruc_negocio":el:["ruc"]
        },bd_negocios))
        return respuesta
    
    def eliminar_negocio(self):
        respuesta=list(filter(lambda el : el["ruc"]!=ruc,bd_tiendas))
        return respuesta



    def actualizar_negocio(self,bd,negocio,ruc,clave,valor):
        
            
    

    def  mostrar_todo(self):
        return tiendas
    





tiendas_objetos = Tienda()
print(tiendas_objetos.filtrar_por_gerente(tiendas,"Nadine"))
print(tiendas_objetos.negocios_con_mas_de_dos_categorias("abarrotes"))
print(tiendas_objetos.mostrar_nombre_y_ruc(tiendas))
print(tiendas_objetos.actualizar_horario_atencion(tiendas))
print(tiendas_objetos.actualizar_horario(tiendas, "2345678901", nuevo_horario))
## tarea 
def actualizar_negocio(self,bd,negocio,ruc,clave,valor):
            pass
## otro metodo para crear un nuevo producto

def agregar_producto(self, nuevo_producto):
    self.productos.append(nuevo_producto)
    
    
## otro metodo para actualizar el horario de atencion 


def actualizar_horario_atencion(self, nuevo_horario):
    self.horario_atencion = nuevo_horario
     
nuevo_horario = {"dia": "8am-1pm", "tarde": "3pm-9pm"}
tiendas.actualizar_horario_atencion(nuevo_horario)


