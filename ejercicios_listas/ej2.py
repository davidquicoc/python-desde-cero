# Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado.
# Copia los elementos de la lista en otra lista pero en orden inverso, y
# muestra sus elementos por la pantalla.

lista = []
copia = []

for indice in range(1,6):
    lista.append(input("Escribe la cadena nº %d: " % indice))

copia = lista[::-1]

for cad in copia:
    print(cad)