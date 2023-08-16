"""1)	Lea en pantalla, el nombre y genero para cuatro personas:
•	Asigne a las mujeres al grupo “A” y anteponga a su nombre: [F] nombre apellido
•	Asigne a las hombres al grupo “B” y anteponga a su nombre: [M] nombre apellido
•	Mencione que genero tuvo mayor frecuencia de apariciones (intentar)
"""

print("Lectura de nombre y genero")

#Definicion de variables

#nom significa nombre
nom1 = 0
nom2 = 0
nom3 = 0
nom4 = 0

#g significa genero
g1 = 0
g2 = 0
g3 = 0
g4 = 0

#Declaracion de variables / Contador masculino y femenino
countM = 0
countF = 0

#Captura de datos

print("\nGénero de las personas: \nMujeres: F \nHombres: M")

nom1 = input("\nIngrese el nombre y apellido de la primera persona: ")
g1 = input("Ingrese el genero de la primera persona: ")

nom2 = input("\nIngrese el nombre y apellido de la segunda persona: ")
g2 = input("Ingrese el genero de la segunda persona: ")

nom3 = input("\nIngrese el nombre y apellido de la tercera persona: ")
g3 = input("Ingrese el genero de la tercera persona: ")

nom4 = input("\nIngrese el nombre y apellido de la cuarta persona: ")
g4 = input("Ingrese el genero de la cuarta persona: ")

# Procesamiento de datos


if g1 == "f":
    print("\nLa persona [F] {} pertenece al grupo A".format(nom1))
    countF = countF + 1
elif g1 == "m":
    print("\nLa persona [M] {} pertenece al grupo B".format(nom1))
    countM = countM + 1
else:
    print("\nEl genero es invalido para la primera persona, favor intentar de nuevo")

if g2 == "f":
    print("\nLa persona [F] {} pertenece al grupo A".format(nom2))
    countF = countF + 1
elif g2 == "m":
    print("\nLa persona [M] {} pertenece al grupo B".format(nom2))
    countM = countM + 1
else:
    print("\nEl genero es invalido para la segunda persona, favor intentar de nuevo")

if g3 == "f":
    print("\nLa persona [F] {} pertenece al grupo A".format(nom3))
    countF = countF + 1
elif g3 == "m":
    print("\nLa persona [M] {} pertenece al grupo B".format(nom3))
    countM = countM + 1
else:
    print("\nEl genero es invalido para la tercera persona, favor intentar de nuevo")

if g4 == "f":
    print("\nLa persona [F] {} pertenece al grupo A".format(nom4))
    countF = countF + 1
elif g4 == "m":
     print("\nLa persona [M] {} pertenece al grupo B".format(nom4))
     countM = countM + 1
else:
    print("\nEl genero es invalido para la cuarta persona, favor intentar de nuevo")

if countM == countF:
    print("\nHay una igual cantidad de personas con generos opuestos")
elif countM > countF:
    print("\nHay mas personas con genero masculino, dado que hay {} con genero masculino".format(countM))
elif countM < countF:
    print("\nHay mas personas con genero femenino, dado que hay {} con genero femenino".format(countF))
else:
    print("\nOpcion invalida, no se pueden contar los generos")

# No sé como contar los generos