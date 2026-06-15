# Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que
# de la siguiente información:
# 
# La temperatura media de cada día
# Los días con menos temperatura
# Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima
# coincide con ella.
# 
# Si no existe ningún día se muestra un mensaje de información.

temperaturas = []
for indice in range(1,6):
    temperatura = []
    temperatura.append(int(input("Día %d. Temperatura máxima: " % indice)))
    temperatura.append(int(input("Día %d. Temperatura mínima: " % indice)))
    temperaturas.append(temperatura)

print("\nTemperaturas medias")
indice = 1
for temperatura in temperaturas:
	print("Día %d. Temperatura media: %f:" % (indice, sum(temperatura) / len(temperatura)))
	indice += 1

temperatura_minima = temperaturas[0][1];
for temperatura in temperaturas:
	if temperatura[1] < temperatura_minima:
		temperatura_minima = temperatura[1]

print("\nDías con menos temperatura")
indice = 1
for temperatura in temperaturas:
	if temperatura[1] == temperatura_minima:
		print("Día %d" % indice)
	indice +=1
	
existe_temperatura = False
print("\nDías con temperatura máxima")
temp_max = int(input("Introduce una temperatura: "))
indice = 1
for temperatura in temperaturas:
	if temperatura[0] == temp_max:
		print("Día %d" % indice)
		existe_temperatura = True
	indice +=1
if not existe_temperatura:
	print("No hay ningún día con dicha temperatura.")
