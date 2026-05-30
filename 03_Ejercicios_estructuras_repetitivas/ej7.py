# Realizar una algoritmo que muestre la tabla de multiplicar
# de un número introducido por teclado.

num = int(input("Introduce un número: "))

for n in range(1, 11):
    print(num, " x ", n , " = ", num * n ,sep="")