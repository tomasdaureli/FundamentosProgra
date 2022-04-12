# FUNCIONES
def burbuja(lista):
    '''Orden mediante el metodo burbuja'''
    ordenado = False
    recorrido = 1
    while ordenado == False:
        ordenado = True
        for i in range(len(lista)-recorrido):
            if lista [i] > lista [i+1]:
                aux = lista [i+1]
                lista [i+1] = lista [i]
                lista [i] = aux
                ordenado = False
        recorrido = recorrido + 1
    return lista

def azarlista():
    '''Generar lista de numeros al azar.'''
    import random
    l = []
    for lista in range(0,10):
        N = random.randint(1,20)
        l.append(N)
    print("Lista:",l)
    return l

# PROGRAMA PRINCIPAL
fin = azarlista()
lis = burbuja(fin)
print("Lista ordenada:",lis)