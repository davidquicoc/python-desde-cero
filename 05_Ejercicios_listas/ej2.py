# Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado.
# Copia los elementos de la lista en otra lista pero en orden inverso, y muestra
# sus elementos por la pantalla.

lista = []
lista_inversa = []

for indice in range(1,6):
    lista.append(input("Introduce la cadena %d: " % indice))

lista_inversa = lista[::-1]

for cadena in lista_inversa:
    print(cadena)