# FUNCIONES
def legajorep(lista,n,i):
    '''Validar que el legajo no haya sido ingresado anteriormente.'''
    j = 0
    encontrado = False
    if i != 0:
        while j < len(lista) and encontrado == False:
            if lista[j] == n:
                encontrado = True
            j = j + 1
    return encontrado

def aprobados(notas):
    cant = 0
    i = 0
    for i in range(len(notas)):
        if notas[i] >= 4:
            cant = cant + 1
        i = i + 1
    return cant
    
def desaprobados(notas):
    cant = 0
    i = 0
    for i in range(len(notas)):
        if notas[i] < 4:
            cant = cant + 1
        i = i + 1
    return cant

def promedionota(notas):
    suma = 0
    i = 0
    for i in range(len(notas)):
        suma = suma + notas[i]
        i = i + 1
    promedio = suma / len(notas)
    return promedio

def superan(legajo,notas,promedio):
    i = 0
    print("Los legajos que superan el promedio son ",end="")
    for i in range(len(notas)):
        if notas[i] > promedio:
            print(legajo[i],end=", ")
        i = i + 1

def listaordenada(legajo,notas):
    i = 0
    ordenado = False
    while ordenado == False:
        ordenado = True
        for i in range(0,len(legajo)-1):
            for j in range(i+1,len(legajo)):
                if legajo[i] > legajo[j]:
                    auxL = legajo[j]
                    auxN = notas[j]
                    legajo[j] = legajo[i]
                    notas[j] = notas[i]
                    legajo[i] = auxL
                    notas[i] = auxN
                    ordenado = False
                i = i + 1
                j = j + 1
    print("\n______________")
    print("Lista ordenada")
    print(legajo)
    print(notas)
                    
# PROGRAMA PRINCIPAL
legajos = []
nota_final = []
indice = 0
legajo = int(input("Ingrese legajo(-1 para finalizar): "))
while legajo != -1:
    while legajo < -1:
        print("El legajo debe ser mayor a 1.")
        legajo = int(input("Ingrese legajo(-1 para finalizar): "))
    if legajo != -1:
        noRep = legajorep(legajos,legajo,indice)
        while noRep == True:
            print("El legajo ya ha sido ingresado.")
            legajo = int(input("Ingrese legajo(-1 para finalizar): "))
            while legajo < -1:
                print("El legajo debe ser mayor a 1.")
                legajo = int(input("Ingrese legajo(-1 para finalizar): "))
            noRep = legajorep(legajos,legajo,indice)
        if legajo != -1:
            legajos.append(legajo)
            notaFinal = float(input("Ingrese la nota final: "))
            while notaFinal < 0 or notaFinal > 10:
                notaFinal = float(input("Error, la nota debe estar comprendida entre 0 y 10. Ingrese la nota final: "))
            nota_final.append(notaFinal)
            legajo = int(input("Ingrese legajo(-1 para finalizar): "))
    indice = indice + 1
print(legajos)
print(nota_final)
cantAp = aprobados(nota_final)
print("Cantidad de aprobados:",cantAp)
cantDes = desaprobados(nota_final)
print("Cantidad de desaprobados:",cantDes)
promedio = promedionota(nota_final)
print("El promedio de notas es",promedio)
legsup = superan(legajos,nota_final,promedio)
orden = listaordenada(legajos,nota_final)