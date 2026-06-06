# Suponiendo que hemos introducido una cadena por teclado que representa una
# frase (palabras separadas por espacios), realiza un programa que cuente
# cuantas palabras tiene.

contador = 0
posicion = 0
cadena = input("Introduce una cadena: ")

cadena = cadena.strip()

posicion = cadena.find(" ", posicion)
while posicion != -1:
    contador += 1
    while cadena[posicion + 1] == " ":
        posicion += 1
    posicion = cadena.find(" ", posicion + 1)

print("La frase tiene", contador + 1, "palabras")