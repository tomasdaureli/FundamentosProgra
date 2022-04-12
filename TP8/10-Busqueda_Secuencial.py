# FUNCIONES
def azarlista(x,y):
    '''Generar lista de numeros al azar.'''
    import random
    l = []
    for lista in range(x,y + 1):
        N = random.randint(x,y)
        l.append(N)
    return l
    
def busquedasecuencial(l,x):
    '''Buscar un valor en una lista y devolver la posicion en donde se encuentra'''
    i = 0
    encontrado = False
    while i < len(l) and encontrado == False:
        if l[i] == x:
            encontrado = True
            print("El valor se encuentra en la posicion",i)
        i = i + 1
    return encontrado



# PROGRAMA PRINCIPAL
desde = int(input("Desde: "))
hasta = int(input("Hasta: "))
fin = azarlista(desde,hasta)
print(fin)
buscar = int(input("Ingrese el valor que desea encontrar: "))
buscarFn = busquedasecuencial(fin,buscar)
if buscarFn == False:
    print("El valor no se encuentra en la lista.")