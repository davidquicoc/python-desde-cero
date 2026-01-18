# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a
# otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

horas = int(input("Hora: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
tiempo_viaje = int(input("Tiempo de viaje en segundos: "))

seginicial = horas * 3600 + minutos * 60 + segundos;

segfinal = seginicial + tiempo_viaje

horallegada = (segfinal // 3600) % 24;
minllegada = (segfinal % 3600) // 60;
segllegada = segfinal % 60;

print("Hora de llegada:")
print(horallegada,":",minllegada,":",segllegada)