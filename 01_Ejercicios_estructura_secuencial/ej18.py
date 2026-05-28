# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input("Nombre: ")
apellido1 = input("Primer apellido: ")
apellido2 = input("Segundo apellido: ")

iniciales = nombre[0] + apellido1[0] + apellido2[0]

print("Iniciales:",iniciales.upper())