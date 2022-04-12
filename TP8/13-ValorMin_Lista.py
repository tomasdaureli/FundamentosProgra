import random
lista = []
minimo = 100
num = random.randint(0,100)
pos = 0
while num != 0:
    lista.append(num)
    if num < minimo:
        minimo = num
    num = random.randint(0,100)
print(lista)
print("El valor minimo de la lista fue",minimo,end=". ")
print("Y se encontro en la/s posicion/es",end=" ")
while pos != len(lista):
    if lista[pos] == minimo:
        print(pos,end=", ")
    pos = pos + 1