# crear un sistema de para gestion de control de stock de productos
#casos de uso
#historia de usuario
#producto ower
#baclobg
#MVP
#prototipo de mierda

#ENTIDADES INTITIS
# La base de datos sobre la que voy a trabajar

productos=[
    {
        "id":1,
        "codigo":"2023_A"
        "nombre":"arroz",
        "descripcion":"costeño costal x 100k",
        "stock":5,
        "unidad":"costales",
        "precio":125,
        "moneda":"soles"
        
    
    }
]



# casos de usos
class Producto:
    #atributos de instancia
    def _init_(self,nombre,descripcion,stock,unidad,precio,moneda="soles"):
        self.nombre=nombre
        self.descripcion=descripcion
        self.stock=stock
        self.unidad=unidad
        self.precio=precio
        self.moneda=moneda
    #creacion de metodos
    def mostrar_productos(self):
        mensaje=f"""
        tienes{len(productos)}productos
      
        los productos son:
        {productos}
    """
        return mensaje
    
    
    def registrar_producto(self):
        nuevo_id=len(productos)+1
        codigo="2023_B"
        producto_nuevo={
            
            "id":1,
            "codigo":"2023_B",
            "nuevo_id":nuevo_id,
            "nombre":self.nombre,
            "descripcion":self.descripcion,
           
            "stock":self.stock,
            "unidad":self.unidad,
            "precio":self.precio,
            "moneda":self.moneda
               
        }
        registro_producto=productos.append(producto_nuevo)
        return f"el siguiente producto se registro exitosamente{producto_nuevo}"
    

    
    def mostrar_productos(self,id):
        productos_buscar=productos[id-1]
        return productos_buscar
  
    def eliminar_producto(self,id):
        producto_eliminar=productos.pop[id-1]
        return f"el siguiente producto fue eliminada{producto_eliminar}"
    
    def actualizar_producto(self,id,clave,valor):
        ol=valor
        producto_actualizar=list(filter(lambda obj:obj["clave"]==id,productos))[0].update({clave:valor})
        return "se actualizo"
      #list funcion para crear lista  
        
#["h","o","l","a"]

#programa  funcional en python
#metodo funcional filter retorna una lista con el elemento  que se truede una lista
# funciones anonimos o autoejecutado en python se les conoce como funciones 
# lambda -> funciones  anonimos
# lambda a,b:return a+b  # para ejecutar esta funcion necesito llamar ala variable suma
#suma(3,4)##      
    
    
prod=Producto("aceite","extra grande",2,"botella x litro",12.50)
print(prod.registrar_producto())
print(prod.mostrar_producto())

print(prod.actualizar_productoo(125,"precio"130))
print(prod.mostrar_producto())