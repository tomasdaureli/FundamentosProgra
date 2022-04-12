zona = int(input("Indique la zona geografica del local(1:CABA;2:GBA): "))
recaudacion = 0
suma250 = 0
hombre = 0
sumaH = 0
descuento = 0
ticket = 0
while zona != -1:
    sexo = int(input("Indique el sexo del cliente(1:Masculino;2:Femenino): "))
    if sexo != 1:
        if sexo != 2:
            print("No valido.")
            sexo = int(input("Indique el sexo del cliente(1:Masculino;2:Femenino): "))
    menu = int(input("Indique el menu vendido(1:$250;2:$400;3:$500): "))
    if menu != 1:
        if menu != 2:
            if menu != 3:
                print("No valido.")
                menu = int(input("Indique el menu vendido(1:$250;2:$400;3:$500): "))
    if menu == 1:
        suma250 = suma250 + 1
        ticket = 250
    elif menu == 2:
        ticket = 400
    else:
        ticket = 500
    if sexo == 2:
        ticket = ticket - (ticket * 0.25)
    elif sexo == 1:
        hombre = hombre + 1
        sumaH = sumaH + ticket
    recaudacion = recaudacion + ticket
    zona = int(input("Indique la zona geografica del local(1:CABA;2:GBA): "))
if hombre > 0:
    promedioH = sumaH / hombre
    print("El promedio de compra de los hombres es de $",promedioH,".")
print("Hubo",suma250,"compras del menu 1.")
print("La recaudacion total de la cadena es de $",recaudacion,"teniendo en cuenta los descuentos realizados.")