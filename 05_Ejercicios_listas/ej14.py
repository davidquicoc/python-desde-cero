# Crear un programa que lea los precios de 5 artículos y las cantidades
# vendidas por una empresa en sus 4 sucursales. Informar:
# 
# Las cantidades totales de cada artículo.
# La cantidad de artículos en la sucursal 2.
# La cantidad del artículo 3 en la sucursal 1.
# La recaudación total de cada sucursal.
# La recaudación total de la empresa.
# La sucursal de mayor recaudación.

precios = []
cantidades = []

num_articulos = 5
num_sucursales = 4

for indice in range(num_articulos):
    precios.append(float(input("Precio del artículo %d: " % (indice + 1))))

print()

for indice_sucursal in range(num_sucursales):
    cantidad_articulo = []
    for indice_art in range(num_articulos):
        cantidad_articulo.append(int(input("Cantidad del artículo %d, en sucursal %d: " % (indice_art + 1, indice_sucursal + 1))))
    cantidades.append(cantidad_articulo)

print("\nCantidades totales de cada artículo:")
for ind in range(0, num_articulos):
    suma = 0
    for cant_sucursal in cantidades:
        suma += cant_sucursal[ind]
    print("Artículo %d: %d" % (ind + 1, suma))

print("\nTotal sucursal 2: %d" % sum(cantidades[1]))

print("\nSucursal 1, artículo 3: %d" % cantidades[0][2])

total_por_sucursal = []

for indice_sucursal in range(num_sucursales):
    total = 0
    for art in range(num_articulos):
        total += cantidades[indice_sucursal][art] * precios[art]
    total_por_sucursal.append(total)

print("\nRecaudación por sucursal:")
indice_sucursal = 1
for total in total_por_sucursal:
    print("Recaudaciones sucursal %d: %f" % (indice_sucursal, total))
    indice_sucursal += 1


print("\nRecaudación total de la empresa: %f" % sum(total_por_sucursal))

mayorrec = max(total_por_sucursal)

indice_sucursal = 1
for total in total_por_sucursal:
    if total == mayorrec:
        break
    indice_sucursal += 1

print("\nSucursal de mayor recaudación: %d" % indice_sucursal)
