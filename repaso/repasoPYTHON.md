# REPASO PYTHON
## 1. TIPO DE DATOS:
![Alt text](image.png)

un tipo de dato informático o simplemente tipo es un atributo de los datos que indica al ordenador (y/o al programador/programadora) sobre la clase de datos que se va a manejar. Esto incluye imponer restricciones en los datos, como qué valores pueden tomar y qué operaciones se pueden realizar.
Los tipos de datos más comunes son: números enteros, números con signo (negativos), números de coma flotante (decimales), cadenas alfanuméricas (y unicodes), estados, etc.
### CLASE DE TIPOS DE DATOS
**Tipos de datos primitivos (o elementales):**
Los tipos de datos hacen referencia al tipo de información que se trabaja, donde la unidad mínima de almacenamiento es el dato, también se puede considerar como el rango de valores que puede tomar una variable durante la ejecución del programa.
- "a" # string cadena texto 
- "hola" # esto tambien es un string
- "hola soy un string y te saludo" # cadena larga 
# OBSERVACION: todo lo q este entre comillas es un string
- "100"
- "false"
- "hola"
# un string puede estar entre comillas simples o dobles 
- 100 ## este es un tipo de dato numerico entero 
- 2.2 ## este es un tipo de dato numerico de tipo flotante float 
- false ## este es un tipo booleano falso
- true ## tipo de dato booleano verdadero 
## 2. VARIABLES:
es un conjunto de valores que tienen una caracteristica en comun y que responden a unas operaciones determinadas.
- es donde almacenamos nuestro tipo de dato
- esos datos pueden mutar cambiar modificarse
- como creamos una variable para almacenar nuestros datos
  
1. darle un nombre significativo o relacionado al dato que estamos almacenando 
2. indicarle a que dato esta relacionado -> asignacion =
3. indicar el tipo de dato que se va almacenar -> darle el dato a guardar 
   
- primero el dato voy a pedir la edad de yadira 
edad_yadira=18
- el nombre de un alumno 
nombre_alumno="yadira"
## 3. OPERADORES:
1. **operadores aritmeticos**
 - suma +
- resta - 
- multiplicacion *
- divicion /
```python

#suma
suma=45+12
#resta
resta=45-12
#multiplicacion
multi=2*5
#divicion
divi=4/2
operacion=(45+12+23)/4
 op=15+12+14+13+/4
```
 # precedencia de operadores 

**operadores de uso especial**

```python
suma=45+42 #operador suma resultado 87
suma="45"+12 #cocatenacion holamundo
saludo="hola"+"mundo"#concatenacion holamundo 
saludo="hola"+" "+"mundo"#concatenar hola mundo 
saludos="hola"*2 #holahola
```
## 4. DATOS ESTRUCTURADOS:
### **listas**:
 puede almacenar distintos tipos de datos en una sola lista separados por comas :
```python
lista=["nombre",10,False]
lista_amigos=["yadira","medina","azurza","chinita"]
```
**objetos**

tambien al igual que las listas almacenan distintos tipos de datos pero con un orden 
#para almacenar datos en un objeto necesitamos especificar un indice y un valor clave -> valor
```python
{
    "nombre":"jory", 
    "edad":52,
    "sexo":"tos los dias "
 }
```

**combinar ambas estructuras de datos**
```python
alumno0={
    "nombre":"jori",
    "edad":30,
    "amigos":["antony","edwin","china"],
    "direccion":{
        "departamento":"ayacucho",
        "provincia":"lucanas",
        "distrito":"puquio",
        "jiron":"san pedro",
        "numero":152
    }
}
alumnos=[{},{},{}]
```

# CONTROLES DE FLUJO :

## desiciones :
- solo se ejecuta el codigo si cumple o si la condicion es verdadarera, podemos hacer que si la condicion sea falsa se ejecute otro codigo
- sintaxis
- primero espesificar el codigo que se ejecutara si cumple una condicion 
```python
if <condicion>:
     el codigo que deseamos ejecutar si la condicion es verdad
    print("ejecutar esto")
aqui estamos fuera de if o del si este codigo siempre se ejecutara no depende del if 
print("print siempre ejecuta")
```

## si queremos que se ejecute un codigo en caso sea falso
```python
if <condicion falsa>:
    print("solo imprime si es verdad")
else:
    print("solo imprime si es falso")
```
## ejemplo 
```python
if 15>18:
    print("si es verdad imprime esto")
else:
    print("si es falso imprime esto")
```
```python
if 15*2==30
    print("si es verdad imprime esto")
else:
    print("si es falso imprime esto")
```
```python
condicion=True
if condicion:
    print("si es verdad imprime esto")
else:
    print("si es falso imprime esto")
```


# ciclos :
## existen dos tipos 
- cuando sabes la cantidad de veses que vamos repetirpara este caso existe el for
- sintaxis despues de la palabra reservada for deberemos crear una variable que almacene 
-  el numero que iremos iterando.
-  luego tendremos que indicar el rango a iterar a los elementos a iterar
```python
vocales=["a","e","i","o","u"]
for i in vocales:
    print(i)
```
## cuando no sabemos la cantidad de veses a repetir while tambien evalua si la condicion es verdadera 
```python
while true:
     print(hola)

 condicion=true 
 while condicion:
     print("hola")
     texto=input ("ingresa tu nombre o salir para terminar el programa")
     if texto =="salir"
     condicion=False

```
 
# FUNCIONES:
## esta funcion nos muestra el numero mayor de una lista
```python
lista=[45,12,78,3,24,50]
 numero_mayor=max(lista)
 print(numero_mayor)
``` 
## esta funcion nos muestra el numero menor de la lista 
```python
lista=[45,12,78,3,24,50]
 numero_menor=min(lista)
 print(numero_menor)
```
## funcion para convertir de un string a un numero entero
```python
numero_string="100"
 print(type(numero_string))
 numero_entero=int
 int("100")# ->> entero
```
## funcion para convertir un numero a un string
```python
str(100) # ->> "100" ->> string
```
## funcion de python que nos permite agregar elementos al final de una lista
```python
lista=[15,12,78]
 elemento=100
 lista.append(elemento)
 print(lista)
``` 
## funcion de python que nos permite eliminar los elementos q se encuentra al final de una lista
```python
lista=[15,12,78]
 lista.pop()
 print=(lista)
```
## funcion de python que nos permite agregar elementos en cualquier posicion de mi lista para eso se le tiene
### que pasar 2 parametros , primero indicarle el indice y segundo el dato que se va agregar
```python
lista_nombres=["jori","yadira","nadine"]
lista_nombres.insert(1,"satan")
print(lista_nombres
```
## funcion de python que nos permite eliminar elmentos de cualquier posicion de una lista, 
### esta funcion recibe solo el elemnto que deseamos eliminar 
```python
lista=[4,5,6,8,7]
lista.remove(6)
print(lista)
```             
## funcion que nos permite dividir en una lista un acadena
```python
cadena="hola como estan"
lista=cadena.split()
print(lista)
url="www.golle.com/id=70133573"
id=url.split(",")
print(id)
```
# 2. FUNCIONES CREADAS: 
## una funcion son mini programas tambien se le conoce como modulos o fragmentos de codigo 
## de uso exclusivo
## funciones propias 
## pasos para crear una funcion propia 
 1. hacer uso de la palabra recervada def
 2. definir un nombre de funcion que describa que tarea va realizar 
 3. establecer los parametros que resibira la funcion entre parentesis ()
 4. establecer que valor odato va retornar mi funcion con la palabra reservada return 
> observacion =>> tambien podemos hacer uso de la funcion print() para retornar un mensaje en nuestra funcion 
## existen dos tipos de funciones los que no resiben ningun parametro  y los que resiben parametros 
```PYTHON
cadena="hola como estan"
lista=cadena.split()
print(lista)
url="www.golle.com/id=70133573"
id=url.split(",")
print(id)
```
como asemos uso de la funcion??

nombre de la funcion y parentesis

## funcion con parametros 
```PYTHON
def mi_print(texto):
    print(texto)
```
```PYTHON
def mi_print(texto):
    print(texto)

def suma(a,b):
    total=a+b
    return total
mi_print(suma(45,12)) ##==>>>>>>>  57
```
# EJEMPLO
- para q se usa esta funcion 
-  para mostar el valor maximo de una lista 
 ```python
 lista=[42,4,45,78,3,1]
mi_print(max(lista))# ===>>> 78

def mi_max(lista):
    numero_mayor=lista[0]
    for numero in lista:
        if numero > numero_mayor:
            numero_mayor=numero
            return numero_mayor
        mi_print(mi_max(lista))
 ```
# funciones con muchos parametros
```python
def funcion(*muchos_parametros):
    total=0
    for numero in muchos_parametros:
        total=total+numero
        return total
print(funcion(45,12,78,10,20))

def dastos(*args):
    nombre=args[0]
    apellido=args[1]
    edad=[2]
    return f"mi nombre es,{nombre},{apellido}, y mi edad es , {edad}"
print(datos("edwin","apellido","50"))