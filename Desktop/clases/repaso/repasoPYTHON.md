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



### cuando no sabemos la cantidad de veces a repeti