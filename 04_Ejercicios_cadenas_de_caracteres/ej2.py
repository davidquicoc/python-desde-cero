# Realizar un programa que comprueba si una cadena leída por teclado comienza
# por una subcadena introducida por teclado.

cadena = input("Introduce una cadena: ")
subcadena = input("Introduce una subcadena: ")

if subcadena.startswith(cadena):
    print("La cadena comienza igual que la subcadena introducida")
else:
    print("La cadena no comienza igual que la subcadena introducida")