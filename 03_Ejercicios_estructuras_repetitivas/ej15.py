# Una persona adquirió un producto para pagar en 20 meses. El primer mes
# pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar
# un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo
# que pagó después de los 20 meses.

pago_acumulado = 0
pago = 10

for mes in range(1, 21):
    pago_acumulado += pago
    pago *= 2

print("Total de lo que pagó después de los 20 meses:",pago_acumulado)