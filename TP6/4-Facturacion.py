cliente = int(input("Ingrese el nro. de cliente: "))
totalFC = float(input("Ingrese el total de la factura: $"))
# proceso
fecha1 = 10
fecha2 = 15
fecha3 = 20
if fecha1 == 10:
    dto1 = 120
    dto2 = (totalFC * 2) / 100
    dto = 0
    if dto1 > dto2:
        dto = dto1
    elif dto2 > dto1:
        dto = dto2
    else:
        dto = dto1
    vencimiento1 = totalFC - dto
if fecha2 == 15:
    vencimiento2 = totalFC
if fecha3 == 20:
    incremento1 = 150
    incremento2 = (totalFC * 10) / 100
    incremento = 0
    if incremento1 > incremento2:
        incremento = incremento1
    elif incremento2 > incremento1:
        incremento = incremento2
    else:
        incremento = incremento1
    vencimiento3 = totalFC + incremento
print("Cliente:",cliente,
      "\nVenc. 1: $",vencimiento1,
      "\nVenc. 2: $",vencimiento2,
      "\nVenc. 3: $",vencimiento3)