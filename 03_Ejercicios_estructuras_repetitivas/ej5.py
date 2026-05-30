# Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y
# 'NO VOCAL' en caso contrario, el programa termina cuando se introduce un espacio.

car = input("Introduce un carácter (espacio para terminar): ")

while car != "" and car != " ":
    if car.upper() == "A" or car.upper() == "E":
        print("VOCAL")
    else:
        print("NO VOCAL")
    car = input("Introduce otro carácter: ")