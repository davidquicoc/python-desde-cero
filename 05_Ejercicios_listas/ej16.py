# Vamos a crear un programa que tenga el siguiente menú:
# 
# - Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
# - Añadir número de la lista en una posición: Me pide un número y una posición, y si la
#   posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
# - Longitud de la lista: te muestra el número de elementos de la lista.
# - Eliminar el último número: Muestra el último número de la lista y lo borra.
# - Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de
#   ella (la posición se pide a partir de 1).
# - Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
# - Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
# - Mostrar números: Muestra los números de la lista
# - Salir

lista = []

while True:
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir\n")
    
    opcion = int(input("Elije una opción (1-9): "))
    
    if opcion == 1:
        num = int(input("Escribe un número: "))
        lista.append(num)
    elif opcion == 2:
        num = int(input("Escribe un número: "))
        pos = int(input("Escribe una posición (empezando por 1): "))
        print()
        if pos > len(lista):
            print("Posición incorrecta.")
        else:
            lista.insert(pos - 1,num)
    elif opcion == 3:
        print("Longitud de la lista: %d" % len(lista))
    elif opcion == 4:
        if len(lista) > 0:
            lista.pop()
        else:
            print("La lista está vacía.")
    elif opcion == 5:
        pos = int(input("Escribe una posición: "))
        print()
        if pos > len(lista):
            print("Posición incorrecta.")
        else:
            lista.pop(pos - 1)
    elif opcion == 6:
        num = int(input("Escribe un número: "))
        print("\nEl número %d aparece %d veces en la lista." % (num,lista.count(num)))
    elif opcion == 7:
        num = int(input("Escribe un número: "))
        print()
        indice_buscar = 0
        print("Posiciones: ",end="")
        for indice in range(0,lista.count(num)):
            indice_buscar = lista.index(num,indice_buscar)
            indice_buscar += 1
            print(indice_buscar," ",end="")
        print()
    elif opcion == 8:
        for num in lista:
            print(num," ",end="")
        print()
    elif opcion == 9:
        break
    else:
        print("Opción incorrecta.")
    
    print()
