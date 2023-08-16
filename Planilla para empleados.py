"""2)	Una empresa desea realizar la planilla para sus empleados, lea los siguientes valore:
•	Nombre
•	Edad
•	Genero 
•	Salario
•	Nivel de empleado [Junior, Senior y Máster]
"""

print("Calculo de planilla")

# Definicion de variables

BONOBAJO = 0.007

no1 = 0 #no es nombre
ed1 = 0 #ed es edad
año1 = 0
g1= 0 #g es genero
salB1 = 0 #salB es salario bruto
niv1 = 0 #niv es nivel de empleado
emp1DesT = 0 #dest es Descuento total del primer empleado
salN1 = 0 #salN es Salario Neto

no2 = 0 #no es nombre
ed2 = 0 #ed es edad
año2 = 0
g2= 0 #g es genero
salB2 = 0 #salB es salario bruto
niv2 = 0 #niv es nivel de empleado
emp2DesT = 0 #dest es Descuento total
salN2 = 0 #salN es Salario Neto

no3 = 0 #no es nombre
ed3 = 0 #ed es edad
año3 = 0
g3= 0 #g es genero
salB3 = 0 #salB es salario bruto
niv3 = 0 #niv es nivel de empleado
emp3DesT= 0 #dest es Descuento total
salN3 = 0 #salN es Salario Neto

#Las siguientes variables son para guardar los bonos de cumpleaños
#Despues de cumplir la condicion de los rangos de nacimiento

emp1Bono = 0 #Esto es para asingar la variable del bono de cumpleñaos
emp2Bono = 0
emp3Bono = 0

#Las siguientes variables son para los descuentos de ISSS, AFP
# En el caso de RENTA será una constante dada la mulitplicacion

ISSS = 0.03
des1Isss = 0 #Muestra solo cantidad de descuento del ISSS
des2Isss = 0
des3Isss = 0

AFP = 0.0725
des1Afp = 0 #Muestra solo cantidad de descuento del AFP
des2Afp = 0
des3Afp = 0


RENTA0= 0
RENTA1 = 0.10 # El 10% se mantiene dentro de un rango $472.01 - $895.24
RENTA2 = 0.20 # El 20% se mantiene dentro de un rango $895.25 - $2038.10
RENTA3 = 0.30 # El 30% se mantiene dentro de un rango $2038.11 - $99999

# ESTO ES PARA DECLARAR LAS CONSTANTES DEL DESCUENTO DE RENTA POR EMPLEADO
# CON BASE AL RANGO SALARIAL QUE TIENE

emp1DesRenta = 0
emp3DesRenta = 0
emp3DesRenta = 0

BOEDAD1 = 50 #BoEdad es bono de año de nacimiento menor a 1950
BOEDAD2 = 40 #BoEdad es bono de año de nacimiento entre 1951 a 1960
BOEDAD3 = 30 #BoEdad es bono de año de nacimiento entre 1961 a 1970
BOEDAD4= 20 #BoEdad es bono de año de nacimiento entre 1971 a 1990
BOEDAD5 = 10 #BoEdad es bono de año de nacimiento mayor a 1991

# A continuacion será declaradas las variables del bono de empleado

emp1BoNiv = 0
emp2BoNiv = 0
emp3BoNiv = 0

#Las sigueintes constantes son del bono de nivel de empleado
BOJ = 0.013
BOS = 0.017
BOM = 0.020

# Captura de datos

print("\nGénero de los empleados: \nMujeres: F \nHombres: M")
print("\nNivel de los empleados: \nJunior: J \nSenior: S \nMáster: Ma")

no1 = input("\nIngrese el nombre del primer empleado: ")
año1 = int(input("Ingrese el año en que nacio el primer empleado: "))
g1 = input("Ingrese el genero del primer empleado: ")
salB1 = float(input("Ingrese el salario base del primer empleado: "))
niv1 = input("Ingrese el nivel del primer empleado: ")

no2 = input("\nIngrese el nombre del segundo empleado: ")
año2 = int(input("Ingrese el año en que nacio el segundo empleado: "))
g2 = input("Ingrese el genero del segundo empleado: ")
salB2 = float(input("Ingrese el salario base del segundo empleado: "))
niv2 = input("Ingrese el nivel del segundo empleado: ")

no3 = input("\nIngrese el nombre del tercer empleado: ")
año3 = int(input("Ingrese el año en que nacio el tercer empleado: "))
g3 = input("Ingrese el genero del tercer empleado: ")
salB3 = float(input("Ingrese el salario base del tercer empleado: "))
niv3 = input("Ingrese el nivel del tercer empleado: ")

# Procesamiento de datos

#I.	Calcule el año en que nació el empleado, Asignar un bono dependiendo de su año de nacimiento

# ESTO ES PARA EL CALCULO DE SOLO EL EMPLEADO 1 PARA EL BONO DE CUMPLEAÑOS
if año1 >= 1900 and año1 <= 2004:
    if año1 >= 1900 and año1 <= 1950:
        print("\nEl bono de año de nacimiento es {} para {}".format(BOEDAD1,no1))
        emp1Bono=BOEDAD1
    elif año1 >= 1951 and año1 <= 1960:
        print("\nEl bono de año de nacimiento es {} para {}".format(BOEDAD2,no1))
        emp1Bono=BOEDAD2
    elif año1 >= 1961 and año1 <= 1970:
        print("\nEl bono de año de nacimiento es {} para {}".format(BOEDAD3,no1))
        emp1Bono=BOEDAD3
    elif año1 >= 1971 and año1 <= 1990:
        print("\nEl bono de año de nacimiento es {} para {}".format(BOEDAD4,no1))
        emp1Bono=BOEDAD4
    elif año1 >= 1991 and año1 <= 2004:
        print("\nEl bono de año de nacimiento es {} para {}".format(BOEDAD5,no1))
        emp1Bono=BOEDAD5
else:
    print("\nEl año de nacimiento se encuentra fuera del rango")

# ESTO ES PARA EL CALCULO DE SOLO EL EMPLEADO 2 PARA EL BONO DE CUMPLEAÑOS
if año2 >= 1900 and año2 <= 2004:
    if año2 >= 1900 and año2 <= 1950:
        print("\nEl bono de año de nacimiento es {} para {}".format(BOEDAD1,no2))
        emp2Bono=BOEDAD1
    elif año2 >= 1951 and año2 <= 1960:
        print("\nEl bono de año de nacimiento es {} para {}".format(BOEDAD2,no2))
        emp2Bono=BOEDAD2
    elif año2 >= 1961 and año2 <= 1970:
        print("\nEl bono de año de nacimiento es {} para {}".format(BOEDAD3,no2))
        emp2Bono=BOEDAD3
    elif año2 >= 1971 and año2 <= 1990:
        print("\nEl bono de año de nacimiento es {} para {}".format(BOEDAD4,no2))
        emp2Bono=BOEDAD4
    elif año2 >= 1991 and año2 <= 2004:
        print("\nEl bono de año de nacimiento es {} para {}".format(BOEDAD5,no2))
        emp2Bono=BOEDAD5
else:
    print("\nEl año de nacimiento se encuentra fuera del rango")

# ESTO ES PARA EL CALCULO DE SOLO EL EMPLEADO 3 PARA EL BONO DE CUMPLEAÑOS
if año3 >= 1900 and año3 <= 2004:
    if año3 >= 1900 and año3 <= 1950:
        print("\nEl bono de año de nacimiento es {} para {}".format(BOEDAD1,no3))
        emp3Bono=BOEDAD1
    elif año3 >= 1951 and año3 <= 1960:
        print("\nEl bono de año de nacimiento es {} para {}".format(BOEDAD2,no3))
        emp3Bono=BOEDAD2
    elif año3 >= 1961 and año3 <= 1970:
        print("\nEl bono de año de nacimiento es {} para {}".format(BOEDAD3,no3))
        emp3Bono=BOEDAD3
    elif año3 >= 1971 and año3 <= 1990:
        print("\nEl bono de año de nacimiento es {} para {}".format(BOEDAD4,no3))
        emp3Bono=BOEDAD4
    elif año3 >= 1991 and año3 <= 2004:
        print("\nEl bono de año de nacimiento es {} para {}".format(BOEDAD5,no3))
        emp3Bono=BOEDAD5
else:
    print("\nEl año de nacimiento se encuentra fuera del rango")

print("--------------------------------------------------------------------------")

#Calculo de edad

ed1 = (2023 - año1)

print("\nLa edad de {} es: {}".format(no1,ed1))

ed2 = (2023 - año2)

print("\nLa edad de {} es: {}".format(no2,ed2))

ed3 = (2023 - año3)

print("\nLa edad de {} es: {}".format(no3,ed3))

print("--------------------------------------------------------------------------")

#Validacion de genero

if g1 == "f":
    print("\nEl empleado {} es mujer".format(no1))
elif g1 == "m":
    print("\nEl empleado {} es hombre".format(no1))
else:
    print("\nEl genero es invalido para la primera persona, favor intentar de nuevo")

if g2 == "f":
    print("\nEl empleado {} es mujer".format(no2))
elif g2 == "m":
    print("\nEl empleado {} es hombre".format(no2))
else:
    print("\nEl genero es invalido para la primera persona, favor intentar de nuevo")

if g3 == "f":
    print("\nEl empleado {} es mujer".format(no3))
elif g3 == "m":
    print("\nEl empleado {} es hombre".format(no3))
else:
    print("\nEl genero es invalido para la primera persona, favor intentar de nuevo")

print("--------------------------------------------------------------------------")

#Validacion de niveles

#II.Realice los descuentos de AFP, RENTA e ISSS, si el salario neto (luego de aplicarle 
# únicamente los descuentos) es menor a $450 otorgar un bono del 0.7% de su salario base


#Calculo de descuento de renta por rango salarial, por empleado

#Empleado numero 1
if salB1 >364:
    if salB1 > 364 and salB1 < 472.01:
        emp1DesRenta = RENTA0
    elif salB1 >= 472.01 and salB1 < 895.25:
        emp1DesRenta = salB1 * RENTA1
    elif salB1 >= 895.25 and salB1 < 2038.11:
        emp1DesRenta = salB1 * RENTA2
    elif salB1 >= 2038.11 and salB1 < 9999:
        emp1DesRenta = salB1 * RENTA3

    des1Isss = salB1 * ISSS
    des1Afp = salB1 * AFP

    emp1DesT = des1Isss + des1Afp + emp1DesRenta
    salN1 = salB1 - emp1DesT + emp1Bono

    print("Descuentos y bonos Primer empleado:")
    print("\nEl descuento de ISSS es: {}, \nEl descuento de AFP es: {} \nEl descuento de renta es: {}".format (des1Isss,des1Afp,emp1DesRenta))
    print("\n El bono respectivo de cumpleaños es: {}".format(emp1Bono))
    print("\n El descuento total es: {} \nEl salario neto es: {}".format(emp1DesT,salN1))

    print("--------------------------------------------------------------------------")

#III.	si el salario neto (luego de aplicarle únicamente los descuentos) es menor a $450 otorgar un bono 
# del 0.7% de su salario base

    if salN1 < 450:
        salN1 = salN1 + salN1 * BONOBAJO
        print("\n Nuevo salario del primer empleado, dado lo bajo que fue : {}".format(salN1))
else:
    print("\nEl salario del primer empleado es demasiado bajo")


#Empleado numero 2
if salB2 >364:
    if salB2 > 364 and salB2 < 472.01:
        emp2DesRenta = RENTA0
    elif salB2 >= 472.01 and salB2 < 895.25:
        emp2DesRenta = salB2 * RENTA1
    elif salB2 >= 895.25 and salB2 < 2038.11:
        emp2DesRenta = salB2 * RENTA2
    elif salB2 >= 2038.11 and salB2 < 9999:
        emp2DesRenta = salB2 * RENTA3

    des2Isss = salB2 * ISSS
    des2Afp = salB2 * AFP

    emp2DesT = des2Isss + des2Afp + emp2DesRenta
    salN2 = salB2 - emp2DesT + emp2Bono

    print("Descuentos y bonos Segundo empleado:")
    print("\nEl descuento de ISSS es: {}, \nEl descuento de AFP es: {} \nEl descuento de renta es: {}".format (des2Isss,des2Afp,emp2DesRenta))
    print("\n El bono respectivo de cumpleaños es: {}".format(emp2Bono))
    print("\n El descuento total es: {} \nEl salario neto es: {}".format(emp2DesT,salN2))
    print("--------------------------------------------------------------------------")

#III.	si el salario neto (luego de aplicarle únicamente los descuentos) es menor a $450 otorgar un bono 
# del 0.7% de su salario base

    if salN2 < 450:
        salN2 = salN2 + salN2 * BONOBAJO
        print("\n Nuevo salario del segundo empleado, dado lo bajo que fue : {}".format(salN2))
else:
    print("\nEl salario del segundo empleado es demasiado bajo")


#Empleado numero 3
if salB3 >364:
    if salB3 > 364 and salB3 < 472.01:
        emp3DesRenta = RENTA0
    elif salB3 >= 472.01 and salB3 < 895.25:
        emp3DesRenta = salB3 * RENTA1
    elif salB3 >= 895.25 and salB3 < 2038.11:
        emp3DesRenta = salB3 * RENTA2
    elif salB3 >= 2038.11 and salB3 < 9999:
        emp3DesRenta = salB3 * RENTA3

    des3Isss = salB3 * ISSS
    des3Afp = salB3 * AFP

    emp3DesT = des3Isss + des3Afp + emp3DesRenta
    salN3 = salB3 - emp3DesT + emp3Bono

    print("Descuentos y bonos Tercer empleado:")
    print("\nEl descuento de ISSS es: {}, \nEl descuento de AFP es: {} \nEl descuento de renta es: {}".format(des3Isss,des3Afp,emp3DesRenta))
    print("\n El bono respectivo de cumpleaños es: {}".format(emp3Bono))
    print("\n El descuento total es: {} \nEl salario neto es: {}".format(emp3DesT,salN3))
    print("--------------------------------------------------------------------------")

#III.	si el salario neto (luego de aplicarle únicamente los descuentos) es menor a $450 otorgar un bono 
# del 0.7% de su salario base

    if salN3 < 450:
        salN3 = salN3 + salN3 * BONOBAJO
        print("\n Nuevo salario del tercer empleado, dado lo bajo que fue : {}".format(salN3))
else:
    print("\nEl salario del tercer empleado es demasiado bajo")


#IV.	En base a su nivel de empleado se deberá otorgar un bono:
# Junior 1.3%
# Senior 1.7%
# Master 2.0%

#Calculo del bono con base al nivel

#Empleado 1

if niv1 == "j" or niv1 == "s" or niv1 == "ma":
    if niv1 == "j":
        emp1BoNiv = salN1 * BOJ
        print("\nEl bono del primer empleado como Junior es: {}".format(emp1BoNiv))
    elif niv1 == "s":
        emp1BoNiv = salN1 * BOS
        print("\nEl bono del primer empleado como Senior es: {}".format(emp1BoNiv))
    elif niv1 == "ma":
        emp1BoNiv = salN1 * BOM
        print("\nEl bono del primer empleado como Master es: {}".format(emp1BoNiv))
    

    salN1 = emp1BoNiv + salN1
    print("\nEl salario final del primer empleado, despues del bono por nivel es {}".format(salN1))

else:
    print("\nNo se pudo calcular el bono del nivel del primer empleado")

print("--------------------------------------------------------------------------")

#Empleado 2

if niv2 == "j" or niv2 == "s" or niv2 == "ma":
    if niv2 == "j":
        emp2BoNiv = salN2 * BOJ
        print("\nEl bono del segundo empleado como Junior es: {}".format(emp2BoNiv))
    elif niv2 == "s":
        emp2BoNiv = salN2 * BOS
        print("\nEl bono del segundo empleado como Senior es: {}".format(emp2BoNiv))
    elif niv2 == "ma":
        emp2BoNiv = salN2 * BOM
        print("\nEl bono del segundo empleado como Master es: {}".format(emp2BoNiv))
    

    salN2 = emp2BoNiv + salN2
    print("\nEl salario final del segundo empleado, despues del bono por nivel es {}".format(salN2))

else:
    print("\nNo se pudo calcular el bono del nivel del segundo empleado")

print("--------------------------------------------------------------------------")

#Empleado 3

if niv3 == "j" or niv3 == "s" or niv3 == "ma":
    if niv3 == "j":
        emp3BoNiv = salN3 * BOJ
        print("\nEl bono del tercer empleado como Junior es: {}".format(emp3BoNiv))
    elif niv3 == "s":
        emp3BoNiv = salN3 * BOS
        print("\nEl bono del tercer empleado como Senior es: {}".format(emp3BoNiv))
    elif niv3 == "ma":
        emp3BoNiv = salN3 * BOM
        print("\nEl bono del tercer empleado como Master es: {}".format(emp3BoNiv))
    

    salN3 = emp3BoNiv + salN3
    print("\nEl salario final del tercer empleado, despues del bono por nivel es {}".format(salN3))

else:
    print("\nNo se pudo calcular el bono del nivel del tercer empleado")


print("--------------------------------------------------------------------------")
