# Programa que declare tres listas 'lista1', 'lista2' y 'lista3' de cinco enteros
# cada uno, pida valores para 'lista1' y 'lista2' y calcule lista3 = lista1 + lista2.

lista1 = []
lista2 = []
lista3 = []

for indice in range(1,6):
	lista1.append(int(input("Número %d para la lista1: " % indice)))

print()

for indice in range(1,6):
	lista2.append(int(input("Número %d para la lista2: " % indice)))

print()

for indice in range(0,5):
	lista3.append(lista1[indice] + lista2[indice])

print("Suma de las listas:")
for numero in lista3:
	print(numero," ",end="")
