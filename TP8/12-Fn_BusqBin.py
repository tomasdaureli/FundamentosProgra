# FUNCIONES
def azarlista():
    '''Generar lista de numeros al azar.'''
    import random
    l = []
    for lista in range(0,10):
        N = random.randint(1,20)
        l.append(N)
    print("Lista:",l)
    return l

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

def busquedabin(lista,dato):
    '''Busca un dato mediante busqueda binaria.'''
    izq = 0
    der = len(lista)-1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if lista[centro] == dato:
            pos = centro
        elif lista[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
    if pos == -1:
        print("El numero no esta en la lista.")
    else:
        print("El numero esta en la posicion",pos)
    return pos
    
# PROGRAMA PRINCIPAL
fin = azarlista()
lis = burbuja(fin)
print("Lista ordenada:",lis)
num = int(input("Numero a buscar: "))
sinExito = 0
exito = 0
while num != -1:
    nro = busquedabin(lis,num)
    if nro == -1:
        sinExito = sinExito + 1
    else:
        exito = exito + 1
    num = int(input("Numero a buscar: "))
print("Busquedas con exito:",exito)
print("Busquedas sin exito:",sinExito)