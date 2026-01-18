# La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de
# tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos,70 céntimos, y
# a partir del décimo minuto, 50 céntimos.
# Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %.

# Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

tiempo = int(input("¿Cuánto tiempo ha durado la llamada (minutos)?: "))
es_domingo = input("¿Es domingo? (S/N): ").upper()

if tiempo <= 5:
    coste_base = tiempo * 100
elif tiempo <= 8:
    coste_base = 500 + (tiempo - 5) * 80
elif tiempo <= 10:
    coste_base = 500 + 240 + (tiempo - 8) * 70
else:
    coste_base = 500 + 240 + 140 + (tiempo - 10) * 50

if es_domingo == "S":
    impuesto = coste_base * 0.03
else:
    turno = input("¿Qué turno: Mañana o Tarde? (M/T)?: ").upper()
    if turno == "M":
        impuesto = coste_base * 0.15
    else:
        impuesto = coste_base * 0.10

total_centimos = coste_base + impuesto

print("Costo de la llamada (sin impuestos):", coste_base / 100, "euros.")
print("Impuesto aplicado:", impuesto / 100, "euros.")
print("Total final a pagar:", total_centimos / 100, "euros.")