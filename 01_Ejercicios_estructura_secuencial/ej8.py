# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor
# desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza
# en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones

sueldo_base = float(input("Sueldo base: "))

venta1 = float(input("Precio de la venta 1: "))
venta2 = float(input("Precio de la venta 2: "))
venta3 = float(input("Precio de la venta 3: "))

comision = venta1 * 0.1 + venta2 * 0.1 + venta3 * 0.1
total_ventas = sueldo_base + comision

print("Comisión por ventas:",comision)
print("Sueldo total:",total_ventas)