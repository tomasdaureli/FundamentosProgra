print("~~~~~~~~~~~~~~~~~~~~")
print("~NOTAS EXAMEN FINAL~")
print("~~~~~~~~~~~~~~~~~~~~\n")
# variables
legajo = int(input("Nro. de legajo (-1 para finalizar): "))
aprobados = 0
desaprobados = 0
aplazados = 0
total = 1
while legajo != -1:
    nota = int(input("Nota: "))
    while nota < 0 or nota > 10:
        print("Error.")
        nota = int(input("Nota: "))
    if nota >= 4:
        print("Aprobado.")
        aprobados = aprobados + 1
    elif nota < 4:
        print("Desaprobado.")
        desaprobados = desaprobados + 1
    elif nota == 1:
        print("Desaprobado.")
        aplazados = aplazados + 1
    total = total + 1
    legajo = int(input("Nro. de legajo (-1 para finalizar): "))
porcAplazos = (aplazados // total) * 100
print("\n")
print(aprobados,"alumnos aprobaron.")
print(desaprobados,"alumnos desaprobaron.")
print("El",porcAplazos,"% de la clase fue aplazado.")