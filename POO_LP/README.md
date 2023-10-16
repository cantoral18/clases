# programacion orientado a objetos(POO)
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
    print(llamandoNadine.llamra("ollanta"))
    ```