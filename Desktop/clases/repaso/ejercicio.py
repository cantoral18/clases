#CREAR UN PROGRAMA QUE ME PIDA LA EDAD DE UNA PERSONA SI LA EDAD ES MAYOR O IGUAL
# A 18 QUE MUESTRE UN MENSAJE "ERES MAYOR DE EDAD"CASO CONTRARIO QUE 
# MUESTRE UN MENSAJE "ERES MENOR DE EDAD"

# edad=int(input("ingrese su edad"))
# if edad>18:
#     print("eres mayor de edad")
# else:
#     print("eres menor de edad")


# #UNA TIENDA COMERCIAL DESEA HACER UN DESCUENTO DEL 20% CREAR UN PROGRAMA QUE ME DETERMINE SIE EL
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


#crear un programa que me pida 5 veces un nombre y por cada vez que 
#lo pida muestre la cantidad de veces que ingreso el nombre


# for n in range(1,6):
#     nombre=input("ingrese nombre:")
#     print( f"ingresastes {n} veces el nombre")

#crear un programa que pida un numero y lo evalue con el numero premiado si el numero
#ingresado es premiado el programa facilicitara si el numero ingresado es 
#incorrecto el programa seguira pidiendo el numero premiado

numero_ganador=56
condicion=True
while condicion:
    numero_ingresado=int(input("ingrese un numero :"))
    if numero_ingresado == numero_ganador:
        print ("ganastes")
        condicion=False
    else:
        print("sihgue intentando")


