# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Realice
# un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule cuánto
# pagó la empresa por los N empleados.

horas_acumuladas = 0
trabajadores = int(input("Nº de trabajadores que tiene la empresa: "))
sueldo_por_hora = float(input("Sueldo por hora: "))

for trabajador in range(1, trabajadores + 1):
    horas_por_semana = int(input("Horas que trabajo el trabajador %d: " % trabajador))
    horas_acumuladas += horas_por_semana
    print("El trabajador %d tiene de sueldo %.2f" % (trabajador,horas_por_semana*sueldo_por_hora))

print("El pago a los %d trabajadores es: %.2f" % (trabajadores,horas_acumuladas*sueldo_por_hora))