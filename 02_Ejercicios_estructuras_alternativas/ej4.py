# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es
# cero, o un mensaje de aviso en caso contrario.

dividendo = int(input("Nº1: "))
divisor = int(input("Nº2: "))

if divisor == 0:
    print("El segundo número no debe ser 0")
else:
    print("Resultado = %.0f" % (dividendo/divisor))