# De una empresa de transporte se quiere guardar el nombre de los conductores que
# tiene, y los kilómetros que conducen cada día de la semana.
# 
# Para guardar esta información se van a utilizar dos arreglos:
# 
# Nombre: Lista para guardar los nombres de los conductores.
# kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
# Se quiere generar una nueva lista ("total_kms") con los kilómetros totales que
# realza cada conductor.
# 
# Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.

dias =["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
nombre = []
kms = []

while True:
    num_conductores = int(input("Nº de conductores que tiene la empresa: "))
    if num_conductores > 0: break

for indice_cond in range(0,num_conductores):
    nombre.append(input("Nombre del conductor %d: " % (indice_cond + 1)))
    kms_dias = []
    for indice_dias in range(0,7):
        kms_dias.append(int(input("Kms realizado el día %s: " % dias[indice_dias])))
    kms.append(kms_dias)

total_kms = []
for km in kms:
    total_kms.append(sum(km))

for nombre, total in zip(nombre, total_kms):
    print(nombre, "ha realizado", total, "kms")
