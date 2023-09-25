# funciones de python mas usadas
## tres de las funciones más utilizadas en Python y que debes dominar son list, type y tuple.

- **List()**. Con esta función se puede crear un listado y aportan un gran nivel de flexibilidad al trabajar con conjuntos de datos.
- **Type().** Se trata de una función básica de Python que se utiliza principalmente con objetivos de depuración de código.
- **Tuple().** Permiten crear una lista, pero con dos características diferentes (inmutabilidad, pues sus valores no pueden ser modificados, y      rapidez, pues su uso acelera el proceso de cálculo).

1. **Sentencia def**
Esta definición de función se usa para crear objetos, las cuales son definidas por cada usuario. Son sentencias para ejecutar con el nombre de la función y tienen referencias al nombre o namespace local o global.

2. **Argumentos y parámetros**
La definición de una función en Python con valores, denominados parámetros, se pueden convertir en argumentos cuando interviene una llamada de los valores.


3. **Argumentos indeterminados**
Dentro de las funciones de Python te brinda la opción de utilizar parámetros indeterminados por posición y nombre. Esto te ayuda en las ocasiones en donde no has definido la cantidad de elementos que necesitas para tu función.

4. **Sentencia pass**
Las funciones en Python te permiten efectuar una operación nula, es decir, que cuando se emplea no sucede nada. Esto te puede ayudar cuando una sentencia se requiere de manera sintáctica y no necesita de un código para efectuarse.


5. **Sentencia return**
La sentencia return te ayuda a que las funciones se puedan comunicar con el exterior. Esto se da gracias a la devolución de valores. En Python tienes la posibilidad de retornar valores múltiples separados en comas. A su vez, se puede registrar a distintas variables y valores de la tupla inmutable.

###averiguar sobre entornos virtuales en python

# ¿Qué es un entorno virtual de python? 

Según Python, «un entorno virtual es un entorno de Python parcialmente aislado que permite instalar paquetes para que los use una aplicación en particular, en lugar de instalarlos en todo el sistema.

# ¿Por qué usar entornos virtuales en python?
Si es la primera vez que escuchas sobre un entorno virtual, puedes darte una idea de como funciona de la siguiente manera: supongamos que tenemos un computador en donde se le ha instalado python y además tenemos instaladas librerías como OpenCV, numpy, entre otros… solo por dar un pequeño ejemplo.  

Y es entonces que hemos incursionado en algunos proyectos, en los cuales vamos a trabajar con las mismas librerías pero con versiones diferentes. 

Entonces, ¿qué hacemos?, instalar cierta versión de la librería, probar el código de uno de los proyectos, desinstalar dicha librería y ahora instalarla, pero con otra versión para probar el código de un segundo proyecto? 
# Cómo instalar virtualenv?
En esta ocación vamos a usar virtualenv para la creación de los entornos virtuales. Este no es un módulo estándar (no viene incluido en python) por lo que necesitaremos instalarlo, para ello vamos a usar pip. Entonces nos dirigimos al símbolo del sistema en windows y digitamos:
```python
pip install virtualenv
```
Importante: Para este tutorial asumiré que en nuestro computador tenemos instalado Python.
# ¿Cómo crear un entorno virtual?
Lo primero que tenemos que hacer antes de crear el entorno virtual es ubicarnos en directorio donde queramos que se cree dicho entorno. Ya que estamos en el símbolo del sistema, usaremos el comando cd, que nos permitirá movernos al path deseado.

Una vez que estemos ubicados en dicho path, vamos a digitar:

virtualenv nombre_del_entorno_virtual
Es decir que para crear el entorno virtual necesitaremos de virtualenv, seguido del nombre que le queramos dar.

Una vez que se presione enter, se creará el entorno virtual. En el símbolo del sistema tendremos un mensaje indicándonos que este se ha creado exitosamente. Mientras que en el directorio donde lo hemos creado, tendremos una nueva carpeta con el nombre del entorno virtual, y dentro podremos encontrar varias carpetas y archivos.

Voy a mostrarte un ejemplo de este procedimiento a continuación:
![Alt text](image.png)
En la figura 1 he enumerado dos líneas. En la número 1, me estoy dirigiendo al directorio en donde deseo crear el entorno virtual, por ello uso el comando cd, para realizar el cambio de directorio. En mi caso voy a crear mi entorno virtual en la carpeta Proyecto1, que está en el escritorio.

Una vez allí voy a proceder con la creación del entorno virtual, para ello he digitado virtualenv p1, que quiere decir que crearemos un entorno virtual llamado p1.

Al dar enter, después de unos segundos nos aparecerá un mensaje el cual indica que el entorno ha sido creado exitosamente.