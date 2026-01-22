# Algoritmo que pida números hasta que se introduzca un cero.
# Debe imprimir la suma y la media de todos los números introducidos.

suma = 0
cont = 0

num = int(input("Introduce un número: "))

while num != 0:
    suma = suma + num
    cont = cont + 1
    num = int(input("Introduce un número: "))

if cont > 0:
    media = suma / cont
else:
    media = 0

print("Suma:",suma)
print("Media:",media)