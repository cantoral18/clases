# tipos de datos primitivos 
"a" # string cadena texto 
"hola" # esto tambien es un string
"hola soy un string y te saludo" # cadena larga 
## OBSERVACION: todo lo q este entre comillas es un string
"100"
"false"
"hola"
# un string puede estar entre comillas simples o dobles 
100 ## este es un tipo de dato numerico entero 
2.2 ## este es un tipo de dato numerico de tipo flotante float 
#false ## este es un tipo booleano falso
#true ## tipo de dato booleano verdadero 

# variables
# es donde almacenamos nuestro tipo de dato
# esos datos pueden mutar cambiar modificarse
## como creamos una variable para almacenar nuestros datos
#1. darle un nombre significativo o relacionado al dato que estamos almacenando 
#2. indicarle a que dato esta relacionado -> asignacion =
#3. indicar el tipo de dato que se va almacenar -> darle el dato a guardar 
# primero el dato voy a pedir la edad de maritza
edad_maritza=18
##el nombre de un alumno 
nombre_alumno="maritza"

## operadores 
#1. operadores aritmeticos 
#suma +
#resta - 
#multiplicacion *
#divicion /
#suma
suma=45+12
#resta
resta=45-12
#multi
multi=2*5
#divi
divi=4/2
operacion=(45+12+23)/4
op=15+12+14+13+/4
# precedencia de operadores 

#operadores de uso especial 
suma=45+42 #operador suma resultado 87
suma="45"+12 #cocatenacion holamundo
saludo="hola"+"mundo"#concatenacion holamundo 
saludo="hola"+" "+"mundo"#concatenar hola mundo 
saludos="hola"*2 #holahola

#datos estructurados 
## listas
# puede almacenar distintos tipos de datos en una sola lista separados por comas 
lista=["nombre",10,False]
lista_amigos=["yadira","medina","azurza","chinita"]
## objetos
#tambien al igual que las listas almacenan distintos tipos de datos pero con un orden 
#para almacenar datos en un objeto necesitamos especificar un indice y un valor clave -> valor
{
    "nombre":"jory", 
    "edad":52,
    "sexo":"tos los dias "
 }
#combinar ambas estructuras de datos 
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


# CONTROLES DE FLUJO
## desiciones
### solo se ejecuta el codigo si cumple o si la condicion es verdaderapodemos hacer si la condicion sea falasa ejecute otro codigo
#### primero especificar el codigo si cumple una condicion
#_________________________________________________________________________

if <condicion>:
    ## el codigo que deseamos ejecutar si la condicion es verdadera
    print ("ejecuta esto")
##aqui estamos fuera del if o del si este codigo siempre se ejecutara no depende de if
print("esto siempre ejecuta")
#_______________________________________________________________________

#si queremos que se ejecute un codigo en caso que sea falso
if <condicion falsa>:
    print("solo imprime si es verdad")
else:
    print("solo imprime si es falso")
    
###EJEMPLO
```python
if 15>18:
    print("si es verdad imprime esto")
else:
    print("si es falso imprime esto")

__________________________________________    
if 15*2:
    print("si es verdad imprime esto")
else:
    print("si es falso imprime esto")  

___________________________________________
condicion=True
if condicion:
    print("si es verdad imprime esto")
else:
    print("si es falso imprime esto")  
``````
##ciclos
## existen dos tipos
###  cuando sabes la cantidad de  veces que vamos a repetir
# para este caso existe el for
#sintaxis despues de la palabra reservada for  debemos crear una variable que 
# almacene el numero que iremos iterando.
#luego tendremos que indicar  el rango a iterar alos elementos a iterar
```python

vocales=("a","e","i","o","u")
for i in vocales:
    print(i)

``````

# cuando no sabemos la cantidad de veces a repetir

while  tambien evalua si la condision es verdadera
```python

while true:
    print(hola) 

condicion= true 
while condicion:
    print("hola")
    texto=input ( "ingresa tu nombre o salir para terminar el programa:")
    if texto =="salir":
        condicion=false
 ```
 # funciones 
##existen 2  tipos  
### 1. PROPIAS DE LENGUAJE         :
### ya vienen creadas e insertadas en python y estas listas para ser usadas
## estructura de una funcion
## tiene el nombre seguido de una parentisis
### dentro de un parentesis podremos pasarles datos que necesita la funcion para ejecutarse
```python
**esta es una funcion para mostrar por consola datos**
print()
## esta funcion nos permite saber la longitud de una lista o unstring 
**len nos devuelve un numero**
print(len)
````


# ##ciclos
### existen dos tipos
 ###  cuando sabes la cantidad de  veces que vamos a repetir
 para este caso existe el for
sintaxis despues de la palabra reservada for  debemos crear una variable que 
 almacene el numero que iremos iterando.
luego tendremos que indicar  el rango a iterar alos elementos a iterar
vocales=("a","e","i","o","u")
for i in vocales:
    print(i)


 cuando no sabemos la cantidad de veces a repetir
while  tambien evalua si la condision es verdadera
while true:
    print(hola) 
    
condicion= true 
while condicion:
    print("hola")
         texto=input ( "ingresa tu nombre o salir para terminar el programa:")
     if texto =="salir":
         condicion=false
        
        
#  esta funcion nos muestra el numero mayor de una lista
lista=[45,23,22,3,21]
numero_mayor=max(lista)
print(numero_mayor)

esta funcion nos muestra el numero menor de una lista 
lista=[45,23,22,3,21]
numero_menor=min(lista)
print(numero_menor)

#funciones para convertir de un string a numero entero 
```python
int("100")#->>100->> entero
```
 funcion para convertir un entero a un strimg
str(100) #->> "100"->>string   

funcion de python que nos permite agregar elementos al final de una lista 
```python
lista=[15,12,78]
elemento=100
lista.append(elemento)
print(lista) 
   ```
# funcion que nos permite eliminar los elementos que se encuentran al final de una lista
```python
 lista=[15,12,78] 
 lista.pop()
 print(lista)
print (eliminado)
```
 #funcion de python que nos permite agregar elementos en cualquier  posicion de mi 
 lista para eso se le tiene que pasar dos parametros
 ,primero indicar el indice y segundo el datoque se va agregar   
```python
 lista_monbres=["jory","luis","pepe"]
 lista_monbres.inst(1,"carlos")
 print(lista_monbres)
```
 funcion de python que nos permite eliminar elementos de cualquier
 posicion de una lista ,esta funcion recibe solo el elemento que deseamos eliminar
```python
lista=[4,3,5,6,8]
 lista.remove(6)
 print (lista)

 #funcion que nos permite dividir en un acadena
 cadena="hola como estan"
 lista=cadena.split()
 print(lista)
url="www.golle.com/id=70133573"
id=url.splip("=").pop()
print(id)
```
# 2. FUNCIONES CREADAS
 FUNCIONES PROPIAS
PASOS PARA CREAR UNA FUNCION PROPIA
1. hacer uso de la palabra reservada
 2. defenir un nombre de funcion que describa que tarea va a realizar
3. establecer los parametros que resivira la funcion entre parentisis()
 4. establecer que valor o dato va retornar mi funcion con la palabra reservada return
 >observacion =>> tambien podemos hacer uso de la funcion print (para retornar un mensaje en nuestra funcion)
 retornar un mensaje en nuestra function
 existen 2 tipos de funciones los que resiven ningun parametro
 y los que resven prarmetro
 ```python
 def saludo()
     print("hola este es un saludo")
```
 como hacemos uso de la function
nombre de la funciones y parentesis
```python
funcion con parametros
 def mi_print(texto)
   print(texto)


 
 print("hola este es print de python")
 mi_print("hola este es mi print creado")
 def suma(a,b)
  total=a+b
  return total
  mi_print(suma(45,12)) ##==>>>>> 57
 

#ejemplo 


 para que se usa esta funcion 
  para mostrar` el valor maximo de una lista
 ```python
 lista=[12,4,43,56,78]
 mi_print(max(lista)) #===>>>78
 
 def mi_max(lista):
     numero_mayor=lista[0]
     for numero in lista:
         if numero> numero_mayor:
             numero_mayor=numero
     return numero_mayor
 mi_print(mi_max(lista))
    
 def mi_min(lista):
     numero_menor=lista[0]
     for numero in lista:
         if numero> numero_menor:
             numero_menor=numero
     return numero_menor
 mi_print(mi_min(lista))
```
# funcion es con muchos parametros
```python
 def funciones(*muchos_parametros):
     total=0
     for numero in muchos_parametros:
         total=total+numero
    return total
 print( funciones(45,52,85,96))

def datos(*args):
    nombre=args[0]
    apellido=args[1]
    edad=args[2]
    return f"mi nombre es ,{nombre},{apellido}y mi edad es,{edad}"
print(datos("luis","apellido","50"))
    
    ```