# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math

cateto1 = float(input("Cateto 1:"))
cateto2 = float(input("Cateto 2:"))

hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
print("La hipotenusa es",hipotenusa)