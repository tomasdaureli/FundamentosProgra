# Simulacro
# 1 pto. c/ $100
# +10 ptos. cuando compra mayor a $3000
print("===================================")
print("= Programa para puntos acumulados =")
print("===================================")
print('\n')
importe = int(input("Ingresar el importe de la compra (0 para finalizar): $"))
while importe < 0:
    print("Error. El importe ingresado no es válido. Intente nuevamente.")
    importe = int(input("Ingresar el importe de la compra (0 para finalizar): $"))
mayor = 0
ventas = 1
suma = 0
cont50 = 0
orden = 1
while importe != 0:
    suma = suma + importe
    if importe > mayor:
        mayor = importe
        orden = ventas
    puntos = importe // 100
    if importe > 3000:
        puntos = puntos + 10
    if puntos >= 50:
        cont50 = cont50 + 1
    print(puntos," puntos obtenidos.")
    ventas = ventas + 1
    puntos = 0
    importe = int(input("Ingresar el importe de la compra (0 para finalizar): $"))
    if importe < 0:
        print("Error. El importe ingresado no es válido. Intente nuevamente.")
        importe = int(input("Ingresar el importe de la compra (0 para finalizar): $"))
promedio = suma / ventas
print("La mayor compra realizada fue de $",mayor," y fue la venta n°",orden)
print("El importe promedio de compras fue de $",promedio)
print(cont50," compras superaron los 50 puntos.")
# no supe como mostrar el orden en el que fue ingresada la compra de mayor valor