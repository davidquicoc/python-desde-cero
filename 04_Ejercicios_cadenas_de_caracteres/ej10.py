# Introducir una cadena de caracteres e indicar si es un palíndromo.
# Una palabra palíndroma es aquella que se lee igual adelante que atrás.

cadena = input("Introduce una cadena: ")

if cadena.lower() == cadena[::-1].lower():
    print(cadena,"es palíndromo")
else:
    print(cadena,"no es palíndromo")