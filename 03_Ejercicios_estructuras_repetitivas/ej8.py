# Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior
# es mayor que el superior lo tiene que volver a pedir. A continuación se van introduciendo números
# hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:
# 
# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# 
# He informa si hemos introducido algún número igual a los límites del intervalo.

suma_dentro_intervalo = 0
cont_fuera_intervalo = 0
igual_limites = False

while True:
    limite_inferior = int(input("Límite inferior del intervalo: "))
    limite_superior = int(input("Límite superior del intervalo: "))

    if limite_inferior > limite_superior:
        print("El límite inferior debe ser menor que el superior.")
    else:
        break;

num = int(input("Introduce un número (0, para salir): "))
while num != 0:
    if num > limite_inferior and num < limite_superior:
        suma_dentro_intervalo += num
    else:
        cont_fuera_intervalo += 1
    
    if num == limite_inferior or num == limite_superior:
        igual_limites = True
    
    num = int(input("Introduce un número (0, para salir): "))

print("Suma de los números dentro del intervalo:",suma_dentro_intervalo)
print("Cantidad de los números fuera del intervalo:",cont_fuera_intervalo)
if igual_limites:
    print("Se introdujo un número igual a los límites del intervalo")
else:
    print("No se introdujo un número igual a los límites del intervalo")