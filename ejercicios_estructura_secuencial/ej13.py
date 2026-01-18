# Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
# Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?

import math

n = float(input("Número: "))

raiz_cuadrada = math.sqrt(n)
raiz_cubica = n ** (1/3)

print("Raíz cuadrada:",raiz_cuadrada)
print("Raíz cúbica:",raiz_cubica)