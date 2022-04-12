# FUNCIONES
def azarlista(x,y):
    '''Generar lista de numeros al azar.'''
    import random
    l = []
    cantN = 0
    cantP = 0
    for lista in range(x,y):
        N = random.randint(x,y)
        if N > 0:
            cantP = cantP + 1
        elif N < 0:
            cantN = cantN + 1
        l.append(N)
    print("Cantidad de positivos en la lista:",cantP)
    print("Cantidad de negativos en la lista:",cantN)
    return l

# PROGRAMA PRINCIPAL
desde = -99
hasta = 99
final = azarlista(desde,hasta)