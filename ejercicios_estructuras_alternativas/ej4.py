# Crea un programa que pida al usuario dos números y muestre su división si el segundo
# no es cero, o un mensaje de aviso en caso contrario.

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))

if n2 == 0:
    print("El segundo número no debe ser 0")
else:
    print("Divisíon:",n1,"/",n2,"=",(n1/n2))