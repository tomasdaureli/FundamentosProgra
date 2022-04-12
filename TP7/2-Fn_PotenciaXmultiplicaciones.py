# FUNCION
def calcularPotencia(a,b):
    '''Potenciar a un numero mediante multiplicaciones sucesivas''' 
    producto = 1
    cont = 0
    while cont != b:
        producto = producto * a
        cont = cont + 1
    return producto