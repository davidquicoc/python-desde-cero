# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
# Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutos = int(input("Minutos: "))

horas = minutos // 60
resto = minutos % 60

print(minutos, "minutos son", horas, "horas y", resto, "minutos")