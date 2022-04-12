import random

fila1 = []
fila2 = []
fila3 = []

for i in range(30):
    legajo = random.randint(0,10000)
    fila1.append(legajo)
for j in range(30):
    materiasAprobadas = random.randint(0,10)
    fila2.append(materiasAprobadas)
i = 0
aprobados = 0
desaprobados = 0
aprobaron10 = 0
aprobaron456 = 0
for f in range(30):
    requisito = (10//2) + 2 #el requisito es aprobar mas de la mitad de materias anuales(10) + 2.
    if fila2[i] > requisito:
        fila3.append(1)
        aprobados = aprobados + 1
        if fila2[i] == 10:
            aprobaron10 = aprobaron10 + 1
        elif fila2[i] >= 4 or fila2[i] <= 6:
            aprobaron456 = aprobaron456 + 1
    else:
        fila3.append(0)
        desaprobados = desaprobados + 1
    i = i + 1
if desaprobados > 0:
    porcentaje = round((desaprobados / 30) * 100,2)
print(fila1)
print(fila2)
print(fila3)
print("1 = Aprobó")
print("0 = Desaprobó")
print("\n")
print("Alumnos aprobados: ",aprobados)
print("Porcentaje de desaprobados: ",porcentaje,"%")
print("Alumnos que aprobaron las 10 materias anuales: ",aprobaron10)
print("Alumnos que aprobaron entre 4 y 6 materias: ",aprobaron456)