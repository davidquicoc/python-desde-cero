# Pide una cadena y un carácter por teclado (valida que sea un carácter) y
# muestra cuantas veces aparece el carácter en la cadena.

cadena = input("Introduce una cadena: ")

while True:
    caracter = input("Introduce un carácter: ")
    if len(caracter) == 1: break

print("Nº veces que aparece el carácter (%s) en la cadena '%s': %i" % (caracter, cadena, cadena.count(caracter)))