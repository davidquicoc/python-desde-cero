# Diseñar el algoritmo correspondiente a un programa, que:
# 
# Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# Carga la tabla con valores numéricos enteros.
# Suma todos los elementos de cada fila y todos los elementos de cada columna
# visualizando los resultados en pantalla.

tabla = []
for ind_fila in range(1,6):
    fila = []
    for ind_columna in range(1,6):
        fila.append(int(input("Nº de fila %d y columna %d: " % (ind_fila, ind_columna))))
    tabla.append(fila)

indice_fila = 1
for fila in tabla:
    print("Suma de los elementos de la fila %d es %d" % (indice,sum(fila)))
    indice += 1

for indice_columna in range(1,6):
	suma = 0
	for fila in tabla:
		suma += fila[indice_columna - 1]
	print("La suma de los elementos de la columna %d es %d" % (indice_columna,suma))
