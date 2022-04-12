# FUNCIONES
def azarlista(x,y):
    '''Generar lista de numeros al azar.'''
    import random
    l = []
    for lista in range(x,y + 1):
        N = random.randint(x,y)
        l.append(N)
    print(l)
    return l
    
    
# PROGRAMA PRINCIPAL
desde = int(input("Desde "))
hasta = int(input("Hasta "))
fin = azarlista(desde,hasta)