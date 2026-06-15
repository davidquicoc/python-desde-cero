# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por
# un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las
# notas, la nota media, la nota más alta que ha sacado y la menor.

notas = []

for num in range(1,6):
    while True:
        nota = float(input("Introduce la nota %d: " % num))
        if nota >= 0 and nota <= 10: break
    notas.append(nota)

print("\nNotas: ",end="")
for n in notas:
    print(n," ",end="")

print()
print("Nota media:",sum(notas)/len(notas))
print("Nota máx.:",max(notas))
print("Nota mín.:",min(notas))