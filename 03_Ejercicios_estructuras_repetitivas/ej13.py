# Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la
# semana (seis días) y requiere determinar el total de éstas, así como el sueldo que
# recibirá por las horas trabajadas.

horas_acumuladas = 0
sueldo_por_hora = float(input("Introduce el sueldo por hora: "))

for dia in range(1, 7):
    horas = int(input("Horas trabajadas en el día %s: " % dia))
    horas_acumuladas += horas

print("Horas acumuladas en la semana:",horas_acumuladas)
print("Sueldo:",sueldo_por_hora * horas_acumuladas)