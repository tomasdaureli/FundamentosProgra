# FUNCIONES
def numeronatural():
    '''Ingresar un numero y validar que sea natural'''
    num = int(input("Ingresar un numero natural: "))
    if num <= 0:
        num = int(input("Error. El numero ingresado no es natural. Intente nuevamente: "))
    return num

# PROGRAMA PRINCIPAL
n = numeronatural()
print(n)