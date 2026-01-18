# Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de
# dos circunferencias y las clasifique en uno de estos estados:

import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))
r1 = float(input("r1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
r2 = float(input("r2: "))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if distancia > (r1 + r2):
    print("Circunferencias exteriores")
elif distancia == (r1 + r2):
    print("Circunferencias tangentes exteriores")
elif distancia < (r1 + r2) and distancia > abs(r1 - r2):
    print("Circunferencias secantes")
elif distancia == abs(r1 - r2):
    print("Circunferencias tangentes interiores")
elif distancia > 0 and distancia < abs(r1 - r2):
    print("Circunferencias interiores")
elif distancia == 0:
    print("Circunferencias concéntricas")