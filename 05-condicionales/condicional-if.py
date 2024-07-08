
# ? condicional if
# ? if condicion:
# ?     codigo
# ? elif condicion:
# ?     codigo
# ? else:
# ?     codigo

# ? operdores de comparacion
# ? == igual
# ?= diferente
# ? < menor que
# ? > mayor que
# ? <= menor o igual que
# ? >= mayor o igual que

# ? Ejemplo 1

print("\n*********************ejemplo 1*******************")


#! color = input("Adivina mi color favorito: ")
color = "rojo"
if color == "rojo":
    print("Enhorabuena!!")
    print("el color es rojo.")
else:
    print("el color es incorecto.")

# ? Ejemplo 2
print("\n**********************ejemplo 2*******************")

# year = 2020
# year = int(input("¿en que año estamos?: "))

if year >= 2021:
    print("Estamos en el 2021 en adelante !!")
else:
    print("Es un año anterior al 2021 !!")

# ? Ejemplo 3
print("\n**********************ejemplo 3 *******************")
nombre = input("¿cual es tu nombre?: ")
edad = int(input("¿cual es tu edad?: "))
ciudad = input("¿en que ciudad vives?: ")
continente = input("¿en que continente vives?: ")
mayoria_edad = 18
if edad >= mayoria_edad:
    print(f"{nombre} eres mayor de edad !!")
    if continente == "europa":
        print("y vives en europa")
    else:
        print("no vives en europa")
