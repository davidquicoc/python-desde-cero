# Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye
# la aparición del primer carácter en la cadena por el segundo carácter.

cadena = input("Introduce una cadena: ")

while True:
    caracter1 = input("Carácter que se va a buscar: ")
    if len(caracter1) == 1: break
while True:
    caracter2 = input("Carácter que se va a sustituir: ")
    if len(caracter2) == 1: break

nueva_cadena = cadena.replace(caracter1,caracter2)

print("Cadena modificada:",nueva_cadena)