# Realizar un programa que compruebe si una cadena contiene una subcadena.
# Las dos cadenas se introducen por teclado.

cadena = input("Introduce una cadena: ")
subcadena = input("Introduce una subcadena: ")

if cadena.find(subcadena) > -1:
    print("La cadena contiene la subcadena")
else:
    print("La cadena no contiene la subcadena")