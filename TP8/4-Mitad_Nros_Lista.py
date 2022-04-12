# FUNCIONES
def azarlista(x,y):
    '''Generar lista de numeros al azar.'''
    import random
    l = []
    lm = []
    suma = 0
    for lista in range(x,y + 1):
        N = random.randint(x,y)
        l.append(N)
        lm.append(N/2)
    print(l)
    print(lm)
    return l 

# PROGRAMA PRINCIPAL
desde = int(input("Desde "))
hasta = int(input("Hasta "))
fin = azarlista(desde,hasta)