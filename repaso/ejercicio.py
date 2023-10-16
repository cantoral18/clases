## 1. crear un programa que me pida la edad de una persona si la edad es mayor o igual a 18 
## que me muestre un mensaje "heres mayor de edad " caso contrario que me muestre un mensaje 
## "heres menor de edad"

# edad = int(input("Por favor, ingrese su edad: "))
# if edad >= 18:
#     print("Eres mayor de edad.")
# else:
#     print("Eres menor de edad.")

## 2. una tienda comercial desea hacer un descuento del 20%, crear un programa que me determine 
## si el cliente se ase acreedor del descuento teniendo encuenta los siguientes, si el cliente realiza una compra de 
## igual o mayor a 1000 soles mostrar un mensaje que diga "ganaste el descuento del 20% ahora pagaras 
## <mostrar el total de la compra menos el descuento>" en caso la compra no supere los 1000 soles entonses mostrar un mensaje 
## que diga "no aplicas al descuento <mostrar el monto de la compra>"
# Solicitar al usuario el monto de la compra

# monto_compra = float(input("Ingrese el monto de la compra en soles: "))
# if monto_compra >= 1000:
#     descuento = 0.20 * monto_compra
#     total_pagar = monto_compra - descuento
#     print(f"Ganaste el descuento del 20%. Ahora pagarás {total_pagar} soles.")
# else:
#     print(f"No aplicas al descuento. El monto de la compra es de {monto_compra} soles.")

## 3. crear un programa q me pida 5 veses un nombre por cada vez que lo pida muestre la cantidad de veses que ingreso el nombre
# for n in range (1,6):
#     nombre=input("ingrese un nombre:")
#     if nombre in nombres:
#         nombres [nombre] +=1
#         print(f"""
#         _____________________________________
#         {nombre}se ingreso {i} de veses.
#         _____________________________________
#         """)
#     print(f"ingresaste {n} veses el nombre")
## 4. crear un programa que pida un numero y lo evalue con el numero premiado si el numero ingresado es el premiado 
## el programa finalizara si el numero ingresado es incorrecto el programa seguira pidiendo el numero premiado
# numero_premiado = 9
# while true:
#     numero_ingresado = int(input("ingresa un numero: "))
#     if numero_ingresado == numero_premiado:
#         print(f"""
#                  felicidades
#         has adivinado el numero premiaado.
# """)
#         break
#     else:
#         print("numero incorrecto. Intetalo de nuevo. ")

# 5. crear una funcion por cada operador aritmetico y que resiva dos parametros y retorne el resultado de la operacion
# ojo crearse un funcion que nos permita imprimir el resultado .
# def mi_print(texto):
#     print(texto)
# def suma(a, b):
#     return a + b
# def resta(a, b):
#     return a - b
# def multiplicacion(a, b):
#     return a * b
# def divicion(a,b):
#     return a/b

# mi_print(suma(4,6))
# mi_print(resta(4,5))
# mi_print(multiplicacion(4,5))
# mi_print(divicion(4,5))

# 6. escribe una funcion que reciba un numero entero positivo y devuelva su factorial
# def factorial(n):
#      if n == 0:
#          return 1
#      else:
#          resultado = 1
#          for i in range(1, n + 1):
#              resultado *= i
#          return resultado
# numero = 5
# resultado = factorial(numero)
# print(f"El factorial de {numero} es {resultado}")

# 7. escribir una funcion que resiba como parametro una lista de numeros y retorne 
# una nueva lista con el cuadro de cada numero de lista ingresada   
# def calcular_cuadrados(lista):
#     cuadrados = []
#     for numero in lista:
#         cuadrado = numero ** 2
#         cuadrados.append(cuadrado)
#     return cuadrados

# numeros = [1, 2, 3, 4, 5]
# cuadrados = calcular_cuadrados(numeros)
# print(f"Lista de números: {numeros}")
# print(f"Lista de cuadrados: {cuadrados}")

# 8. escribir un programa que resiba una cadena de caracteres y debuelva un objeto con cada palabra que contiene y su grecuencia
def contar_frecuencia_palabras(cadena):
    frecuencia_palabras = {}
    palabras = cadena.split()

    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabras] += 1
        else:
            frecuencia_palabras[palabras] = 1

    return frecuencia_palabras

adena = "hola mundo, hola de nuevo"
resultado = contar_frecuencia_palabras(cadena)
print(resultado)
# crear un entorno virtual con venv de python e instalar el framework django para la creacion de app wed
# crear entorno
# activar entorno
# instalar el paquete