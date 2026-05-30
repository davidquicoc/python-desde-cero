# Escribe un programa que diga si un número introducido por teclado es o no primo.
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
# 
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si
# es divisible por algún otro número.

es_primo = True
num = int(input("Número: "))

for n in range(2, num):
    if num % n == 0:
        es_primo = False

if es_primo:
    print(num,"es primo")
else:
    print(num,"no es primo")