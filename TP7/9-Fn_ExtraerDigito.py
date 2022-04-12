# FUNCIONES
def extraerdigito(a,dig):
    '''Extraer un digito de un numero'''
    if a < 0:
        a = -1 * a
    cont = 0
    num = a
    while a > 0:
        if dig == cont:
            num = a % 10
            a = 0
        a = a // 10
        cont = cont + 1
    if dig >= cont:
        num = -1
    if num != -1:
        print("El digito solicitado es el",num)
    else:
        print("El digito solicitado no es valido.")
    return num

# PROGRAMA PRINCIPAL
a = int(input("Ingresa un numero: "))
dig = int(input("Ingresa un numero: "))
digito = extraerdigito(a,dig)