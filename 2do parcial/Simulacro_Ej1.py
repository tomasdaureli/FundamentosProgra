# FUNCIONES
def eliminarnro(lista,nro):
    '''Recibe un numero como parametro, lo busca, y si lo encuentra, lo elimina cada vez que lo encuentre.'''
    cont = 0
    i = 0
    while len(lista) > i:
        if lista[i] == nro:
            lista.pop(i)
            cont = cont + 1
        else:
            i = i + 1
    return cont

# PROGRAMA PRINCIPAL
import random
N = int(input("Indique la longitud de la lista que desea: "))
miLista = []
for i in range(N):
    num = random.randint(10,99)
    miLista.append(num)
print(miLista)
nfind = int(input("¿Que numero desea eliminar de la lista?: ")) 
fn = eliminarnro(miLista,nfind)
print(miLista)
print("El numero fue eliminado",fn,"vez/veces.")