# Algoritmo que pida un número y diga si es positivo, negativo o 0.

num = float(input("Escribe un número: "))

if num == 0:
    print("El número es igual a 0")
else:
    if num > 0:
        print("El número es positivo")
    else:
        print("El número es negativo")