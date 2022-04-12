# FUNCIONES
def digitos(num):
    '''Indicar cantidad de digitos de un numero'''
    if num < 0:
        num = num * (-1)
    cant = 1
    while num > 9:
        num = num // 10
        cant = cant + 1
    return cant

def ultimosdigitos(num,cant):
    '''Devolver digitos de un numero segun sea indicada la cantidad'''
    if num < 0:
        num = num * (-1)
    cantDigitos = digitos(num)
    if cant > cantDigitos:
        print(num)
    else:
        a = num % (10 ** cant)
        print(a)
    return num
    return a

# PROGRAMA PRINCIPAL
n = int(input("Ingresa un numero: "))
dig = int(input("Ingresa la cantidad de digitos que desee: "))
ult = ultimosdigitos(n,dig)
