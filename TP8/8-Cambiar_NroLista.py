# FUNCIONES
def azarlista(x,y):
    '''Generar lista de numeros al azar.'''
    import random
    l = []
    for lista in range(x,y + 1):
        N = random.randint(x,y)
        l.append(N)
    print(l)
    cambio = int(input("Teniendo en cuanta que la primera posicion es 0.¿Que posicion desea cambiar? "))
    l[cambio] = random.randint(x,y)
    print(l)
    return l
    
    
# PROGRAMA PRINCIPAL
desde = int(input("Desde "))
hasta = int(input("Hasta "))
fin = azarlista(desde,hasta)
