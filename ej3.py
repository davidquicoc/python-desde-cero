# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un
# alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la
# nota media, la nota más alta que ha sacado y la menor.

notas = []
for ind in range(1,6):
    while True:
        nota = float(input("Introduce la nota del índice nº %d: " % ind))
        if nota >= 0 and nota <= 10: break
        else: print("Introduciste una nota incorrecta (%d). Vuelva a intentarlo..." % nota);
    notas.append(nota)

print("Notas: ",end="")
for n in notas:
    print(n," ",end="")
print()
print("Nota media:",sum(notas)/len(notas))
print("Nota máx.:",max(notas))
print("Nota mín.:",min(notas))