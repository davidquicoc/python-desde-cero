# Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque
# por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

base = float(input("Base: "))
exponente = abs(int(input("Exponente: ")))
potencia = 1

for var in range(1, exponente + 1):
    potencia *= base

print("Potencia:",potencia)