# Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d.
# El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos
# vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos)
# alcanzará el vehículo más rápido al otro.

v1 = float(input("Velodicad del coche 1 (km/h): "))
v2 = float(input("Velodicad del coche 2 (km/h): "))
distancia = float(input("Distancia entre los coches (km): "))

tiempo = distancia / (v1 - v2)
tiempo = tiempo * 60

print("Tiempo para alcanzarlo",tiempo,"minutos.")