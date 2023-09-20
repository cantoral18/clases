#1.CREAR UN PROGRAMA QUE ME PIDA LA EDAD DE UNA PERSONA SI LA EDAD ES MAYOR O IGUAL
# A 18 QUE MUESTRE UN MENSAJE "ERES MAYOR DE EDAD"CASO CONTRARIO QUE 
# MUESTRE UN MENSAJE "ERES MENOR DE EDAD"

# edad=int(input("ingrese su edad"))
# if edad>18:
#     print("eres mayor de edad")
# else:
#     print("eres menor de edad")


# #2.UNA TIENDA COMERCIAL DESEA HACER UN DESCUENTO DEL 20% CREAR UN PROGRAMA QUE ME DETERMINE SIE EL
# # CLIENTE SE HACE ACREADOR DEL DESCUENTO TENIENDO ENCUENTA LOS SGTS ,SI EL CLIENTE REALIZA UNA COMPRA DE IGUAL 
# # O MAYOR A 1000 SOLES MOSTRAR UN MENSAJE QUE DIGA " GANASTES UN DESCUENTO DE 20% AHORA PAGARS
# # < MOSTRAR EL TOTAL DE LA COMPRA MENOS EL DESCUENTO>" EN CASO LA COMPRA NO SUPERE LOS 1000 SOLES 
# # ENTONCES MOSTRAR UN MENSAJE QUE DIGA " NO APLICA EL DESCUENTO < MOSTRAR EL MONTO DE LA COMPRA>"

# monto_compra = float(input("Ingrese el monto de la compra en soles: "))
# if monto_compra >= 1000:
#     descuento = 0.20 * monto_compra
#     total_pagar = monto_compra - descuento
#     print(f"Ganaste el descuento del 20%. Ahora pagarás {total_pagar} soles.")
# else:
#     print(f"No aplicas al descuento. El monto de la compra es de {monto_compra} soles.")


#3. crear un programa que me pida 5 veces un nombre y por cada vez que 
#lo pida muestre la cantidad de veces que ingreso el nombre


# for n in range(1,6):
#     nombre=input("ingrese nombre:")
#     print( f"ingresastes {n} veces el nombre")

#4 .crear un programa que pida un numero y lo evalue con el numero premiado si el numero
#ingresado es premiado el programa facilicitara si el numero ingresado es 
#incorrecto el programa seguira pidiendo el numero premiado

# numero_ganador=56
# condicion=True
# while condicion:
#     numero_ingresado=int(input("ingrese un numero :"))
#     if numero_ingresado == numero_ganador:
#         print ("ganastes")
#         condicion=False
#     else:
#         print("sihgue intentando")


# 5.crear una funcion para cada operador aritmeticoy que resiva2 parametros y retorne el resultado
# de la operacion ,ojo,crearse una funcion que nos permita imprimir el resultado.

# def mi_print(texto):
#     print(texto)
    
# def resta (a,b):
#     return a-b
# def suma(a,b):
#     return a+b
# def multi(a,b):
#     return a*b
# def divi(a,b):
#     return a/b

# mi_print(resta(14,1))
# mi_print(suma(14,1))
# mi_print(multi(14,1))
# mi_print(divi(14,1))

#ejercio 6
#escriba una funcion que reciba un numero entero y devuelva su factorial

def factorial(n):
    if n ==0:
        return 1
    else:
        resultado = 1
        for i in range (1,n+1):
            resultado= resultado
            
numero=10
resultado=factorial(numero)
print(f"el factorial de {numero} es {resultado}")

#ejercicio 7
# escribir una funcion que resiva como parametro una lista de numeros y 
# retorne una nueva lista con el cuadrado de cada numeron de lista egresados

lista=(2,8,6)
def 


#ejercicio 8
## escribir un programa que reciba una cadaena de caracteres y desvela un
# objeto con cada palabra que tiene  y su frecuencia


    