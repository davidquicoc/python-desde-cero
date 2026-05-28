# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de
# viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine
# la hora de llegada a la ciudad B.

hora_partida = int(input("Hora: "))
min_partida = int(input("Minutos: "))
seg_partida = int(input("Segundos: "))
tiempo_viaje = int(input("Tiempo de viaje en segundos: "))

seginicial = hora_partida * 3600 + min_partida * 60 + seg_partida;

segfinal = seginicial + tiempo_viaje

horallegada = (segfinal // 3600) % 24;
minllegada = (segfinal % 3600) // 60;
segllegada = segfinal % 60;

print("Hora de llegada: ",horallegada,":",minllegada,":",segllegada,sep="")