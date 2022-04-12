# FUNCIONES
def obtener_mes_en_texto(mes):
    '''Expresar en letras un mes segun el numero indicado'''
    mes = mes
    if mes == 1:
        print("El mes indicado es Enero.")
    elif mes == 2:
        print("El mes indicado es Febrero.")
    elif mes == 3:
        print("El mes indicado es Marzo.")
    elif mes == 4:
        print("El mes indicado es Abril.")
    elif mes == 5:
        print("El mes indicado es Mayo.")
    elif mes == 6:
        print("El mes indicado es Junio.")
    elif mes == 7:
        print("El mes indicado es Julio.")
    elif mes == 8:
        print("El mes indicado es Agosto.")
    elif mes == 9:
        print("El mes indicado es Septiembre.")
    elif mes == 10:
        print("El mes indicado es Octubre.")
    elif mes == 11:
        print("El mes indicado es Noviembre.")
    elif mes == 12:
        print("El mes indicado es Diciembre.")
    else:
        print("El numero ingresado no corresponde a un mes.")
    return mes    
#
mes = int(input("Nro. de mes: "))
texto = obtener_mes_en_texto(mes)
