"""3)	Una heladería desea monitorear que tipo de sabores [especiales o tradicionales] son más populares entre sus clientes:
a.	Especiales: limón, maracuyá y frutos rojos
b.	Tradicionales: chocolate, vainilla y napolitano  
c.	Cada sorbete está conformado por la combinación de 2 sabores:
"""

# Dos especiales, resultan en, Sorbete especial
# Dos tradicionales, resultan en, Sorbete tradicional
# Uno de cada sabor, resultan en, Sorbete mixto

#Definicion de variables

print("\nHeladeria de Andrés")

print("\nMenú de sabores")

print("\nEspeciales: \n 1. Limon \n 2. Maracuyá \n 3. Frutos rojos")
print("\nTradicionales: \n 4. Chocolate \n 5. Vainilla \n 6. Napolitano")


sor1 = 0 #sor es sorbete
sor2 = 0

pSab = 0 #pSab es Primer Sabor
sSab = 0 #sSab es Segundo Sabor

ESP = "Especial"
TRA = "Tradicional"
#Captura de datos

pSab =int(input("\nElija un numero del 1 al 6, para escoger su primer sabor de sorbete: "))
sSab =int(input("\nElija un numero del 1 al 6, para escoger su segundo sabor de sorbete: "))

#Procesamiento de datos

if pSab >= 1 and pSab < 7 :
    if pSab == 1 :
        print("\nEl tipo de sabor para el primer elemento es {} y el sabor es Limon".format(ESP))
        sor1 = ESP
    elif pSab == 2 :
        print("\nEl tipo de sabor para el primer elemento es {} y el sabor es Maracuyá".format(ESP))
        sor1 = ESP
    elif pSab == 3 :
        print("\nEl tipo de sabor para el primer elemento es {} y el sabor es Frutos rojos".format(ESP))
        sor1 = ESP
    elif pSab ==  4:
        print("\nEl tipo de sabor para el primer elemento es {} y el sabor es Chocolate".format(TRA))
        sor1 = TRA
    elif pSab == 5 :
        print("\nEl tipo de sabor para el primer elemento es {} y el sabor es Vainilla".format(TRA))
        sor1 = TRA
    elif pSab == 6 :
        print("\nEl tipo de sabor para el primer elemento es {} y el sabor es Napolitano".format(TRA))   
        sor1 = TRA
else:
    print("\nEl numero esta fuera del menu para el primer sabor")

if sSab >= 1 and sSab < 7 :
    if sSab == 1 :
        print("\nEl tipo de sabor para el segundo elemento es {} y el sabor es Limón".format(ESP))
        sor2 = ESP
    elif sSab == 2 :
        print("\nEL tipo de sabor para el segundo elemento es {} y el sabor es Maracuyá".format(ESP))
        sor2 = ESP
    elif sSab == 3 :
        print("\nEl tipo de sabor para el segundo elemento es {} y el sabor es Frutos rojos".format(ESP))
        sor2 = ESP
    elif sSab ==  4:
        print("\nEl tipo de sabor para el segundo elemento es {} y el sabor es Chocolate".format(TRA))
        sor2 = TRA
    elif sSab == 5 :
        print("\nEL tipo de sabor para el segundo elemento es {} y el sabor es Vainilla".format(TRA))
        sor2 = TRA
    elif sSab == 6 :
        print("\nEl tipo de sabor para el segundo elemento es {} y el sabor es Napolitano".format(TRA))
        sor2 = TRA   
else:
    print("\nEl numero esta fuera del menu para el segundo sabor")

print("\nEl primer sabor de tipo es:  {}".format(sor1))
print("\nEl segundo sabor de tipo es:  {}".format(sor2))

if sor1 == ESP and sor2 == ESP:
    print("\nEl resultado de la combinacion es Sorbete especial")
elif sor1 == TRA and sor2 == TRA:
    print("\nEl resultado de la combinacion es Sorbete tradicional")
elif sor1 == ESP and sor2 == TRA:
    print("\nEl resultado de la combinacion es Sorbete mixto")
elif sor1 == TRA and sor2 == ESP:
    print("\nEl resultado de la combinacion es Sorbete mixto")
else:
    print("\nNo se puede determinar el resutlado de la combinacion")


