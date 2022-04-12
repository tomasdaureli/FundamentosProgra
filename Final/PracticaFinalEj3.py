import random

# FUNCIONES
def azar500():
    '''Crear una lista de 500 numeros de 3 digitos.'''
    lista = []
    for i in range(500):
        num = random.randint(100,999)
        lista.append(num)
    return lista

def burbuja(lista):
    '''Orden mediante el metodo burbuja.'''
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

def valoresnoencontrados(lista):
    i = 0
    x = 100
    suma = 0
    for l in range(100,999):
        if lista[i] == x:
            suma = suma + 1
        x = x + 1
    return suma

def valoresunicos(lista):
    suma = 0
    for i in range(0,len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i] == lista[j]:
                suma = suma + 1
    return suma

def igualvalor(lista1,lista2,lista3):
    suma = 0
    for i in range(len(lista1)):
        if lista1[i] == lista2[i] and lista1[i] == lista3[i]:
            suma = suma + 1
    return suma

# PROGRAMA PRINCIPAL
lista1 = azar500()
lista2 = azar500()
lista3 = azar500()
orden1 = burbuja(lista1)
orden2 = burbuja(lista2)
orden3 = burbuja(lista3)
noaparecen1 = valoresnoencontrados(lista1)
noaparecen2 = valoresnoencontrados(lista2)
noaparecen3 = valoresnoencontrados(lista3)
porcentajeNA1 = round((noaparecen1 / 899) * 100,2)
porcentajeNA2 = round((noaparecen2 / 899) * 100,2)
porcentajeNA3 = round((noaparecen3 / 899) * 100,2)
unicos1 = valoresunicos(lista1)
unicos2 = valoresunicos(lista2)
unicos3 = valoresunicos(lista3)
porcentajeA1 = round((unicos1 / 899) * 100,2)
porcentajeA2 = round((unicos2 / 899) * 100,2)
porcentajeA3 = round((unicos3 / 899) * 100,2)
iguales = igualvalor(lista1,lista2,lista3)
porcentajeI = round((iguales / 899) * 100,2)
print("Lista 1: ", orden1)
print("Lista 2: ", orden2)
print("Lista 3: ", orden3)
print("Porcentaje de valores posibles que no aparecen en la lista 1: %",porcentajeNA1)
print("Porcentaje de valores posibles que no aparecen en la lista 2: %",porcentajeNA2)
print("Porcentaje de valores posibles que no aparecen en la lista 3: %",porcentajeNA3)
print('\n')
print("Porcentaje de valores que aparecen una sola vez en la lista 1: %",porcentajeA1)
print("Porcentaje de valores que aparecen una sola vez en la lista 2: %",porcentajeA2)
print("Porcentaje de valores que aparecen una sola vez en la lista 3: %",porcentajeA3)
print('\n')
print("Porcentaje de valores iguales en la misma posicion en las tres listas: %",porcentajeI)