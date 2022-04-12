# ENTRADAS
# M = Cant. maxima de vacantes, N = Nro. de postulantes, Legajo positivo, Puntaje.
# SALIDAS
# a) Mejores puntajes, su legajo, promedio de puntaje de estos postulantes.
# b) Cant. de postulantes que NO lograron entrar.


# PROGRAMA PRINCIPAL
N = int(input("Ingrese la cantidad de postulantes: "))
while N <= 0:
    N = int(input("Ingrese la cantidad de postulantes con un numero positivo: "))
M = int(input("Ingrese la cantidad maxima de vacantes: "))
while M <= 0:
    M = int(input("Ingrese la cantidad maxima de vacantes con un numero positivo: "))
print('\n')
listaLegajos = []
listaPuntajes = []
for i in range(N):
    legajo = int(input("Legajo(numero positivo): "))
    while legajo <= 0:
        legajo = int(input("Legajo(numero positivo): "))
    puntaje = float(input("Puntaje(0 a 100): "))
    while puntaje < 0 or puntaje > 100:
        puntaje = float(input("Puntaje(0 a 100): "))
    listaLegajos.append(legajo)
    listaPuntajes.append(puntaje)
print('\n')
i = 0
ordenado = False
while ordenado == False:
    ordenado = True
    for i in range(len(listaPuntajes)-1):
        for j in range(i+1,len(listaPuntajes)):
            if listaPuntajes[i] < listaPuntajes[j]:
                auxP = listaPuntajes[j]
                auxL = listaLegajos[j]
                listaPuntajes[j] = listaPuntajes[i]
                listaLegajos[j] = listaLegajos[i]
                listaPuntajes[i] = auxP
                listaLegajos[i] = auxL
                ordenado = False
            i = i + 1
            j = j + 1
eliminados = 0
while len(listaPuntajes) != M:
    listaPuntajes.pop()
    listaLegajos.pop()
    eliminados = eliminados + 1
suma = 0
for i in range(len(listaPuntajes)):
    suma = suma + listaPuntajes[i]
    i = i + 1
promedio = suma / M
print("Puntajes: ",listaPuntajes)
print("Legajos: ",listaLegajos)
print("Puntaje promedio: ",promedio)
print("Postulantes rechazados: ",eliminados)