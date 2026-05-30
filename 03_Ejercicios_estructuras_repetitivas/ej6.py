# Escribir un programa que imprima todos los números pares entre
# dos números que se le pidan al usuario.

num_inicial = int(input("Número inicial: "))
num_final = int(input("Número final: "))

for i in range(num_inicial, num_final + 1):
    if i % 2 == 0:
        print(i," ",end="")