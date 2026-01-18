# Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
# Dicha calificación se compone de los siguientes porcentajes:

# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.

parcial1 = float(input("Parcial 1: "))
parcial2 = float(input("Parcial 2: "))
parcial3 = float(input("Parcial 3: "))
examen = float(input("Dime la nota del examen: "))
trabajo = float(input("Trabajo final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

nota_final = promedio_parciales * 0.5 + examen * 0.30 + trabajo * 0.15

print("Nota final:",nota_final)