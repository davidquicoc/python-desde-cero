# Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
# Ejemplo, si se introduce 23 que muestre 32.

n = int(input("Número de dos cifras: "))

decenas = n // 10
unidades = n % 10

invertido = unidades * 10 + decenas
print("Nº invertido:",invertido)