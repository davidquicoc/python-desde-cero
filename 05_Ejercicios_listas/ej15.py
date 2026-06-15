# Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol.
# Para ello vamos a utilizar dos tablas:
# 
# Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de
# cada partido. En la quiniela se indican 15 partidos.
# Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la
# primera se guarda el número de goles del equipo que está guardado en la primera columna de la tabla
# anterior, y en la segunda los goles del otro equipo.
# El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
# 
# ¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?

quiniela = 15
equipos = []
resultados = []

for indice in range(0,quiniela):
    partido = []
    partido.append(input("Nombre del equipo local del partido %d: " % (indice + 1)))
    partido.append(input("Nombre del equipo visitante del partido %d: " % (indice + 1)))
    equipos.append(partido)
    goles = []
    goles.append(int(input("Goles metidos por el equipo %s: " % (partido[0]))))
    goles.append(int(input("Goles metidos por el equipo %s: " % (partido[1]))))
    print()
    resultados.append(goles)

print("\nQuiniela\n")

for partido,goles in zip(equipos,resultados):
	print(partido[0],"-",partido[1],":",end="")
	if goles[0] > goles[1]:
		print("-> 1")
	else:
		if goles[0] < goles[1]:
			print("-> 2")
		else:
			print("-> X")
