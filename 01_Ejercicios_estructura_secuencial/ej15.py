# Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que
# intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

a = input("Valor de A: ")
b = input("Valor de B: ")

aux = a
a = b
b = aux

print("- - - - - - - - - - - -\nValores intercambiados\n- - - - - - - - - - - -")
print("A =", a)
print("B =",b)