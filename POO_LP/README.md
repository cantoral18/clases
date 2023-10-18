<!-- # programacion orientado a objetos(POO)
### EN INGLES ES OBJECT ORIENT PROGRAMING (OOP)
es un paradigma de programacion
**PARADIGMA** - ES UN MODELO, PATRON O EJEMPLO QUE SE DEBE SEGUIR
POO es un modelo de como programar
**OBJETIVO** - es organizar el codigo de manera que se asemeje a como pensamos en la vida real
se basan en objetos 
y en POO un objeto es toda entidad que se pueda escribir atraves de
 **atributos** ylas **funciones**que se puede realizar la entidad

 # ATRIBUTOS DE CLASE  Y ATRIBUTOS DE INSTANCIA
 ## ejemplo de celular
 ```
class celular:
```

* atributo de tipo clase 
* que son iguales para todo los objetos
* que se creen
```
    modelo="smart phone"
```   
* atributos de instancia
* son atributos propios del objeto
* creamos una funcion inicializadora

    ```
    def _init_(self,marca,modelo,imei,nroCelular):
        self.marca=marca
        self.modelo=modelo
        self.imei=imei
        self.nroCelular=nroCelular
    ```    
* funcianalidades
```

    def llamr (self,destino):
        return f"llamando a {destino}"
```
* objeto celular jory
```
    llamandoJory=celular("poco","x5","963258745,"967812364") # instanciando mi clase - creadon
    mi objeto celular
    print(llamandoJory.marca)
    print(llamandoJory.familia)
    print(llamandoJory.llamar("china"))
  ```

* objeto celular nadine
    ```python
    lamandoNadine=celular("alcatel","basico","3698521,"996587424")
    print(llamandoNadine.marca)
    print(llamandoNadine.familia)
    print(llamandoNadine.llamra("ollanta")) -->
    ```


    tarea
     crear una lista con 10 objetos que contengan los datos de las tiendas comerciales
     > ejemplo:
     ```python
    tiendas=[
        {
            "ruc":96325841
            "nombre":"carlos",
            "categoria":["abarrotes","bodega"],
            "horario_atencion":{
                "dia":7am-12m,
                "tarde":2pm-8pm
            }
            "gerente":"manuel"

        }
     ]
     ```

     ## observacion : las categorias sera:4 abarrotes, farmacia,bodega,restaurante
     ##observacion: los gerente solo podran ser los siguientes :
     ale,luis,mary,jhosi

     ##realizae los siguientes ejercicios
     ##crear una clase para tiendas que tenga los siguientes metodos o caso de uso
     1. crear un metodo que me filtre las tiendas que tienen cada gerente
     2. crear un metodo que me muestre los negocios que tiene  mas de dos categorias
     3. crear un metodo que me muestre solo el nombre y ruc de los tiendas