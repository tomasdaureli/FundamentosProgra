# FUNCIONES
def azarlista(x,y):
    '''Generar lista de numeros al azar.'''
    import random
    l = []
    for lista in range(0,5):
        N = random.randint(1,20)
        l.append(N)
    print("Lista:",l)
    return l

def seleccion(lista):
    '''Ordenar lista con metodo de seleccion.'''
    for i in range(0,len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

# PROGRAMA PRINCIPAL
fin = azarlista(1,10)
lis = seleccion(fin)
print("Lista ordenada:",lis)