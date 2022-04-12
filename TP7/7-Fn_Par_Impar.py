# FUNCIONES
def par_impar(a):
    '''Identificar si un numero es par o impar'''
    num = bool(a % 2 == 0)
    print(num)
    return        
# PROGRAMA
num = int(input("Numero: "))
vof = par_impar(num)