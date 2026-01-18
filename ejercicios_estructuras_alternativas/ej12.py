# Escribir un programa que lea un año indicar si es bisiesto.
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

anyo = int(input("Año: "))
if (anyo % 4 == 0 and not (anyo % 100 == 0)) or anyo % 400 == 0:
    print("Año bisiesto")
else:
    print("Año no bisiesto")