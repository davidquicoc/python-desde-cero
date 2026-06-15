# Programa que declare una lista y la vaya llenando de números hasta que
# introduzcamos un número negativo. Entonces se debe imprimir el vector
# (sólo los elementos introducidos).

lista = []

numero = int(input("Introduce un número: "))
while numero >= 0:
    lista.append(numero)
    numero = int(input("Introduce un número: "))

for n in lista:
    print(n," ",end="")