# Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza
# un programa que introduzca el nombre y la edad de cada alumno. El proceso de
# lectura de datos terminará cuando se introduzca como nombre un asterisco (*)
# 
# Al finalizar se mostrará los siguientes datos:
# 
# Todos los alumnos mayores de edad.
# Los alumnos mayores (los que tienen más edad)

nombres = []
edades = []

while True:
    nombre = input("Introduce el nombre del alumno: ")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Introduce la edad del alumno: ")))
    if nombre == "*": break

edad_max = max(edades)

print("\nAlumnos mayores de edad:")
for i in range(len(nombres)):
	if edades[i] >= 18:
		print(nombres[i],"-",edades[i])

print("\nAlumnos mayores:")
for i in range(len(nombres)):
	if edades[i] == edad_max:
		print(nombres[i],"-",edades[i])