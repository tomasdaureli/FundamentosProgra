import random
# FUNCIONES
def burbuja(lista):
    '''Orden mediante el metodo burbuja'''
    ordenado = False
    recorrido = 1
    while ordenado == False:
        ordenado = True
        for i in range(len(lista)-recorrido):
            if lista [i] < lista [i+1]:
                aux = lista [i+1]
                lista [i+1] = lista [i]
                lista [i] = aux
                ordenado = False
        recorrido = recorrido + 1
    return lista

# PROGRAMA PRINCIPAL
lista = []
for j in range(20):
    num = random.randint(0,100)
    lista.append(num)
print(lista)
orden = burbuja(lista)
i = 0
print("Los 5 valores mas altos de la lista son ",end="")
while i <= 5:
    if i == 5:
        print(lista[i],end=".")
    else:
        print(lista[i],end=", ")
    i = i + 1