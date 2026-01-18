# Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
# pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

eu2 = int(input("Monedas de 2€: "))
eu1 = int(input("Monedas de 1€: "))
cnt50 = int(input("Monedas de 50 céntimos: "))
cnt20 = int(input("Monedas de 20 céntimos: "))
cnt10 = int(input("Monedas de 10 céntimos: "))

total = eu2 * 2 + eu1 * 1 + cnt50 * 0.5 + cnt20 * 0.2 + cnt10 * 0.1

print("Total:",total,"€")