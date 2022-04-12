# ENTRADAS: Proveedores, dias de entrega.
# SALIDAS: Proveedores rechazados (segun dias de entrega).
# FUNCIONES
def listado():
    '''Crear un listado de proveedores y su tardanza en dias de entrega.'''
    rechazados = 0
    proveedores = input("Proveedor ('F' para finalizar): ")
    while proveedores != "f" and proveedores != "F":
        dias = int(input("Dias de entrega: "))
        if dias <= 10:
            marca.append(proveedores)
            tiempo.append(dias)
        else:
            print("Proveedor descartado debido a que no cumple con los requisitos establecidos.")
            rechazados = rechazados + 1
        proveedores = input("Proveedor ('F' para finalizar): ")
    return rechazados

def listaordenada(lista1,lista2):
    '''Ordenar listas de menor a mayor.'''
    i = 0
    ordenado = False
    while ordenado == False:
        ordenado = True
        for i in range(0,len(lista2)-1):
            for j in range(i+1,len(lista2)):
                if lista2[i] > lista2[j]:
                    auxD = lista2[j]
                    auxP = lista1[j]
                    lista2[j] = lista2[i]
                    lista1[j] = lista1[i]
                    lista2[i] = auxD
                    lista1[i] = auxP
                    ordenado = False
                i = i + 1
                j = j + 1
    return [lista1,lista2]


# PROGRAMA PRINCIPAL
lista = listado()
orden = listaordenada(lista[0],lista[1])
print("__________________________________________________________")
print("Listado de proveedores (ordenados segun tiempo de entrega)")
print(orden[0])
print(orden[1])
print(lista[2]," proveedor/es fue/fueron rechazado/s.")