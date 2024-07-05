
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

print("**********************ejemplo 1*******************")


# color = input("Adivina mi color favorito: ")
color = "rojo"
if color == "rojo":
    print("Enhorabuena!!")
    print("el color es rojo.")
else:
    print("el color es incorecto.")

# ? Ejemplo 2
print("**********************ejemplo 2*******************")

# year = 2020
year = int(input("¿en que año estamso?: "))

if year >= 2021:
    print("Estamos en el 2021 en adelante !!")
else:
    print("Es un año anterior al 2021 !!")
