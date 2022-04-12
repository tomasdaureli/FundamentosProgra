# ENTRADAS: Proveedores, dias de entrega.
# SALIDAS: Proveedores rechazados (segun dias de entrega).
# FUNCIONES
def listado():
    '''Crear un listado de proveedores, sus presupuestos y su tardanza en dias de entrega.'''
    cantP = int(input("Ingrese la cantidad de proveedores a evaluar: "))
    promedio = float(input("Ingrese un presupuesto promedio de referencia: $"))
    rechazados = 0
    for i in range(cantP):
        proveedores = input("Proveedor: ")
        presupuesto = float(input("Presupuesto: $"))
        dias = int(input("Dias de entrega: "))
        if dias <= 10:
            if presupuesto < promedio:
                marca.append(proveedores)
                tiempo.append(dias)
                dinero.append(presupuesto)
            else:
                print("Proveedor descartado debido a que no cumple con los requisitos establecidos.")
                rechazados = rechazados + 1
        else:
            print("Proveedor descartado debido a que no cumple con los requisitos establecidos.")
            rechazados = rechazados + 1
    return rechazados

def listaordenada(lista1,lista2,lista3):
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
                    auxE = lista3[j]
                    lista2[j] = lista2[i]
                    lista1[j] = lista1[i]
                    lista3[j] = lista3[i]
                    lista2[i] = auxD
                    lista1[i] = auxP
                    lista3[i] = auxE
                    ordenado = False
                i = i + 1
                j = j + 1
                

# PROGRAMA PRINCIPAL
marca = []
tiempo = []
dinero = []
lista = listado()
orden = listaordenada(marca,tiempo,dinero)
print("__________________________________________________________")
print("Listado de proveedores (ordenados segun tiempo de entrega)")
print("Proveedores:",end=' ')
print(marca)
print("Presupuestos:",end=' ')
print(dinero)
print("Dias de entrega:",end=' ')
print(tiempo)
print(lista," proveedor/es fue/fueron rechazado/s.")