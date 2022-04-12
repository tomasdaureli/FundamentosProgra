print("_____")
print("STORE")
print("\n")
cant = int(input("Ingresar la cantidad solicitada del producto (-1 para finalizar): "))
ventas = 1
ventas10 = 0
ventasSin = 0 
while cant < -1:
    print("Error. Vuelva a intentarlo.")
    cant = int(input("Ingresar la cantidad solicitada del producto (-1 para finalizar): "))
while cant != -1:
    precioBase = int(input("Ingresar el precio base: "))
    while precioBase < -1:
        print("Error. Vuelva a intentarlo.")
        precioBase = int(input("Ingresar el precio base: "))
    if cant <= 12:
        precioTotal = precioBase * 1 * cant
        ventasSin = ventasSin + 1
    elif cant > 12 and cant <= 100:
        precioTotal = precioBase * 1 * 12 + (precioBase - ((precioBase * 10) / 100)) * (cant - 12)
    elif cant > 100:
        precioTotal = precioBase * 1 * 12 + (precioBase - ((precioBase * 10) / 100)) * 88 + (precioBase - ((precioBase * 25) / 100)) * (cant - 100)
        ventas10 = ventas10 + 1
    promedio = precioTotal / cant
    print("El valor total de la venta fue de $",precioTotal,"y el precio promedio fue",promedio)
    cant = int(input("Ingresar la cantidad solicitada del producto (-1 para finalizar): "))
    while cant < -1:
        print("Error. Vuelva a intentarlo.")
        cant = int(input("Ingresar la cantidad solicitada del producto (-1 para finalizar): "))
    ventas = ventas + 1
print("Hubo un total de",ventas,"ventas.")
print("Hubo un total de",ventas10,"ventas con descuento del 10%.")
print("Hubo un total de",ventasSin,"ventas sin descuento.")
