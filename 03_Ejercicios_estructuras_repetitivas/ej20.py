# Mostrar en pantalla los N primero número primos. Se pide por teclado
# la cantidad de números primos que queremos mostrar.

import math

while True:
    cantidad_a_mostrar = int(input("Cantidad de números primos a mostrar: "))
    if cantidad_a_mostrar > 0: break

print("1 :  2")
cantidad_mostrados = 1
num = 3

while cantidad_mostrados < cantidad_a_mostrar:
    es_primo = True
    for divisor in range(3, int(math.sqrt(num)) + 1, 2):
        if num % divisor == 0:
            es_primo = False

    if es_primo:
        cantidad_mostrados += 1
        print(cantidad_mostrados, ": ",num)
    num = num + 2 
