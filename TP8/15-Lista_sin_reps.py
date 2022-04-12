import random
# FUNCIONES
def validarN():
    x = int(input("Indique la extension de la lista(maximo 100): "))
    while x > 100 or x < 0:
        print("Error.")
        x = int(input("Indique la extension de la lista(maximo 100): "))
    return x

def validarRep(l,n,i):
    j = 0
    encontrado = False
    if i != 0:
        while j < len(l) and encontrado == False:
            if l[j] == n:
                encontrado = True
            j = j + 1
    return encontrado

# PROGRAMA PRINCIPAL
lista = []
N = validarN()
indice = 0
while len(lista) < N:
    num = random.randint(0,100)
    rep = validarRep(lista,num,indice)
    lista.append(num)
    if rep == True:
        lista.pop()
    indice = indice + 1
print(lista)