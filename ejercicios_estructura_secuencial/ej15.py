# Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie
# los valores de ambas variables y muestre cuanto valen al final las dos variables.

a = input("A: ")
b = input("B: ")

aux = a
a = b
b = aux

print("Valor de A:", a)
print("Valor de B:",b)