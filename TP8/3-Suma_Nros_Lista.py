# FUNCIONES
def azarlista(x,y):
    '''Generar lista de numeros al azar.'''
    import random
    l = []
    suma = 0
    for lista in range(x,y + 1):
        N = random.randint(x,y)
        suma = suma + N
        l.append(N)
    print(l)
    print("La suma de los numeros de la lista es ",suma)
    return l
    return suma 

# PROGRAMA PRINCIPAL
desde = int(input("Desde "))
hasta = int(input("Hasta "))
fin = azarlista(desde,hasta)