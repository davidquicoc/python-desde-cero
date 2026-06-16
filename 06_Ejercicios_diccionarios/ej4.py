# Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las
# notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un
# diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
# 
# El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta
# que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota media
# obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa nos
# dará un error.

alumnos = {}
cantidad = int(input("Cantidad de alumnos: "))

for num in range(cantidad):
    alumno = input("Nombre del alumno: ")
    while alumno in alumnos:
        print("Ya existe un alumno con ese nombre")
        alumno = input("Introduzca de nuevo el nombre del alumno: ")
    notas = []
    nota = int(input("Escribe una nota del alumno %s (negativo para terminar): " % alumno))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Escribe una nota del alumno %s (negativo para terminar): " % alumno))
    alumnos[alumno] = notas.copy()

for alumno, notas in alumnos.items():
    print("%s ha sacado de nota media %.2f" % (alumno, sum(notas) / len(notas)))