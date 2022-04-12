# FUNCION
def calcularMultiplicacion(a,b):
    '''Multiplicar dos numeros usando solo sumas'''
    suma = 0
    cont = 0
    while cont != b:
        suma = suma + a
        cont = cont + 1
    return suma