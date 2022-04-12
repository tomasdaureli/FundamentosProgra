# ENTRADAS: Rango de valores a y b.
# SALIDAS: Lista de numeros enteros ordenada.
import random
# FUNCIONES
def crearlistaAzar(x,y):
    '''Crear lista al azar.'''
    miLista = []
    if x > 0:
        a = 0
        num = random.randint(a,y)
        while len(miLista) < 1:
            if num != 0 and num >= x:
                miLista.append(num)
            else:
                num = random.randint(a,y)
        while num > 0 and num < x:
                num = random.randint(a,y)
        while num != 0:
            miLista.append(num)
            num = random.randint(a,y)
            while num > 0 and num < x:
                num = random.randint(a,y)
    else:
        num = random.randint(x,y)
        while num != 0:
            miLista.append(num)
            num = random.randint(x,y)
    return miLista

def bublesort(miLista):
    '''Ordenar lista mediante el metodo de burbujeo.'''
    ordenado = False
    recorrido = 1
    intercambios = 0
    while ordenado == False:
        ordenado = True
        for i in range(len(lista)-recorrido):
            if lista [i] > lista [i+1]:
                aux = lista [i+1]
                lista [i+1] = lista [i]
                lista [i] = aux
                ordenado = False
                intercambios = intercambios + 1
        recorrido = recorrido + 1
    return intercambios

# PROGRAMA PRINCIPAL
a = int(input("Indique desde que numero desea crear la lista: "))
b = int(input("Indique hasta que numero desea crear la lista: "))
lista = crearlistaAzar(a,b)
print("\nLista: ")
print(lista)
orden = bublesort(lista)
print("\nLista ordenada:")
print(lista)
print("\nSe realizaron",orden,"intercambios.")