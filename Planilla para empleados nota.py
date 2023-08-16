"""2)	Una empresa desea realizar la planilla para sus empleados, lea los siguientes valore:
•	Nombre
•	Edad
•	Genero 
•	Salario
•	Nivel de empleado [Junior, Senior y Máster]
"""

print("Calculo de planilla")

# Definicion de variables

no1 = 0 #no es nombre
ed1 = 0 #ed es edad
año1 = 0
g1= 0 #g es genero
salB1 = 0 #salB es salario bruto
niv1 = 0 #niv es nivel de empleado
desT10 = 0 #dest es Descuento total
desT11 = 0
desT12 = 0
desT13 = 0
salN10 = 0 #salN es Salario Neto
salN11 = 0
salN12 = 0
salN13 = 0

no2 = 0 #no es nombre
ed2 = 0 #ed es edad
año2 = 0
g2= 0 #g es genero
salB2 = 0 #salB es salario bruto
niv2 = 0 #niv es nivel de empleado
desT2 = 0 #dest es Descuento total
salN2 = 0 #salN es Salario Neto

no3 = 0 #no es nombre
ed3 = 0 #ed es edad
año3 = 0
g3= 0 #g es genero
salB3 = 0 #salB es salario bruto
niv3 = 0 #niv es nivel de empleado
desT3 = 0 #dest es Descuento total
salN3 = 0 #salN es Salario Neto

ISSS = 0.03
desIsss = 0 #Muestra solo cantidad de descuento del ISSS
AFP = 0.0725
desAfp = 0 #Muestra solo cantidad de descuento del AFP

RENTA0= 0 # El 0% se mantiene dentro de un rango de $0.01 - $472
desRenta0 = 0
RENTA1 = 0.10 # El 10% se mantiene dentro de un rango $472.01 - $895.24
desRenta1 = 0
RENTA2 = 0.20 # El 20% se mantiene dentro de un rango $895.25 - $2038.10
desRenta2 = 0
RENTA3 = 0.30 # El 30% se mantiene dentro de un rango $2038.11 - $99999
desRenta3 = 0

boEdad1 = 50 #BoEdad es bono de año de nacimiento menor a 1950
boEdad2 = 40 #BoEdad es bono de año de nacimiento entre 1951 a 1960
boEdad3 = 30 #BoEdad es bono de año de nacimiento entre 1961 a 1970
boEdad4 = 20 #BoEdad es bono de año de nacimiento entre 1971 a 1990
boEdad5 = 10 #BoEdad es bono de año de nacimiento mayor a 1991

# Captura de datos

print("\nGénero de los empleados: \nMujeres: F \nHombres: M")
print("\nNivel de los empleados: \nJunior: J \nSenior: S \nMáster: Ma")

no1 = input("\nIngrese el nombre del primer empleado: ")
año1 = int(input("Ingrese el año en que nacio el primer empleado: "))
g1 = input("Ingrese el genero del primer empleado: ")
salB1 = float(input("Ingrese el salario base del primer empleado: "))
niv1 = input("Ingrese el nivel del primer empleado: ")



# Procesamiento de datos

#I.	Calcule el año en que nació el empleado, Asignar un bono dependiendo de su año de nacimiento
if año1 >= 1900 and año1 <= 2004:
    if año1 >= 1900 and año1 <= 1950:
        print("El bono correspondiente es {} para {}".format(boEdad1,no1))
    elif año1 >= 1951 and año1 <= 1960:
        print("El bono correspondiente es {} para {}".format(boEdad2,no1))
    elif año1 >= 1961 and año1 <= 1970:
        print("El bono correspondiente es {} para {}".format(boEdad3,no1))
    elif año1 >= 1971 and año1 <= 1990:
        print("El bono correspondiente es {} para {}".format(boEdad4,no1))
    elif año1 >= 1991 and año1 <= 2004:
        print("El bono correspondiente es {} para {}".format(boEdad5,no1))
else:
    print("\nEl año de nacimiento se encuentra fuera del rango")

#Calculo de edad

ed1 = (2023 - año1)

print("\nLa edad de {} es: {} años".format(no1,ed1))

#Validacion de genero

if g1 == "f":
    print("\nEl empleado {} es mujer".format(no1))
elif g1 == "m":
    print("\nEl empleado {} es hombre".format(no1))
else:
    print("\nEl genero es invalido para la primera persona, favor intentar de nuevo")


#II.Realice los descuentos de AFP, RENTA e ISSS, si el salario neto (luego de aplicarle 
# únicamente los descuentos) es menor a $450 otorgar un bono del 0.7% de su salario base

desIsss = salB1 * ISSS
desAfp = salB1 * AFP

desRenta0 = salB1 * RENTA0
desRenta1 = salB1 * RENTA1
desRenta2 = salB1 * RENTA2
desRenta3 = salB1 * RENTA3

desT10 = desIsss + desAfp + desRenta0
desT11 = desIsss + desAfp + desRenta1
desT12 = desIsss + desAfp + desRenta2
desT13 = desIsss + desAfp + desRenta3

salN10 = salB1 - desT10
salN11 = salB1 - desT11
salN12 = salB1 - desT12
salN13 = salB1 - desT13

if salB1 >= 365:
    if salB1 >= 365 and salB1 <= 472:
        print("\nEl descuento de ISSS es: {} \nel descuento de AFP es: {} \nel descuento de renta es: {}".format (desIsss,desAfp,desRenta0))
        print("El descuento total es {}".format(desT10))
        print("El salario neto es: {}".format(salN10))
    elif salB1 >= 472.01 and salB1 <= 895.24:
        print("\nEl descuento de ISSS es: {} \nel descuento de AFP es: {} \nel descuento de renta es: {}".format (desIsss,desAfp,desRenta1))
        print("El descuento total es {}".format(desT11))
        print("El salario neto es: {}".format(salN11)) 
    elif salB1 >= 895.25 and salB1 <= 2038.10:
        print("\nEl descuento de ISSS es: {} \nel descuento de AFP es: {} \nel descuento de renta es: {}".format (desIsss,desAfp,desRenta2)) 
        print("El descuento total es {}".format(desT12))
        print("El salario neto es: {}".format(salN12))
    elif salB1 >= 2038.11 and salB1 <= 9999:
        print("\nEl descuento de ISSS es: {} \nel descuento de AFP es: {} \nel descuento de renta es: {}".format (desIsss,desAfp,desRenta3)) 
        print("El descuento total es {}".format(desT13))
        print("El salario neto es: {}".format(salN13))
else:
    print("El salario es demasiado bajo")


