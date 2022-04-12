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

l = [10, 12, 12, 50, 23, 12]
print(l)
num = 12
find = eliminarnro(l,num)
print(l)