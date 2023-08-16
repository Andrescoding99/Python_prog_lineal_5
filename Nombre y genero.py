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

if g1 == "f" or g1 == "m" or g2 == "f" or g2 == "m" or g3 == "f" or g3 == "m" or g4 == "f" or g4 == "m":
    if g1 == "f":
        print("La persona F {} pertenece al grupo A".format(nom1))
    elif g1 == "m":
        print("La persona M {} pertenece al grupo B".format(nom1))
    elif g2 == "f":
        print("La persona F {} pertenece al grupo A".format(nom2))
    elif g2 == "m":
        print("La persona M {} pertenece al grupo B".format(nom2))
    elif g3 == "f":
        print("La persona F {} pertenece al grupo A".format(nom3))
    elif g3 == "m":
        print("La persona M {} pertenece al grupo B".format(nom3))
    elif g4 == "f":
        print("La persona F {} pertenece al grupo A".format(nom4))
    elif g4 == "m":
        print("La persona M {} pertenece al grupo B".format(nom4))
else:
    print("El genero es invalido")
