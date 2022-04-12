importe = int(input("Ingrese el importe de la venta (-1 para finalizar): $"))
if importe < -2:
    print("Error. Ingresa nuevamente el importe.")
    importe = int(input("Ingrese el importe de la venta (-1 para finalizar): $"))
total = 0
ventas = 1
while importe != -1:
    total = total + importe
    ventas = ventas + 1
    importe = int(input("Ingrese el importe de la venta (-1 para finalizar): $"))
    if importe < -2:
        print("Error. Ingresa nuevamente el importe.")
        importe = int(input("Ingrese el importe de la venta (-1 para finalizar): $"))
print("El monto total recaudado en el dia fue de $",total)
print("Se relizó un total de",ventas - 1,"ventas.")