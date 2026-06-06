# Si tenemos una cadena con un nombre y apellidos, realizar un programa que
# muestre las iniciales en mayúsculas.

iniciales = ""
posicion = 0

cadena = input("Introduce una cadena: ")

cadena = cadena.strip()

iniciales = iniciales + cadena[0]

posicion = cadena.find(" ", posicion)

while posicion != -1:
    while cadena[posicion + 1] == " ":
        posicion += 1
    iniciales += cadena[posicion + 1]
    posicion = cadena.find(" ", posicion + 1)

print("Iniciales:",iniciales.upper())