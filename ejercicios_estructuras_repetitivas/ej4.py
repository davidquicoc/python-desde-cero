# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
# El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

cont_neg = 0
cont_pos = 0
cont_cero = 0

cant = int(input("Cantidad de número a introducir: "))

for i in range(1, cant + 1):
    print("Número ",i,": ",end="",sep="")
    num = int(input())
    if num > 0: cont_pos += 1
    elif num < 0: cont_neg += 1
    else: cont_cero += 1

print("Números positivos:",cont_pos)
print("Números negativos:",cont_neg)
print("Números igual a 0:",cont_cero)