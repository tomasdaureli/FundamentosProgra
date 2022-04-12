cantAlu = int(input("Ingresar la cantidad de alumnos: "))
while cantAlu < 0:
    print("Error. Cantidad no valida.")
    cantAlu = int(input("Ingresar la cantidad de alumnos: "))
print("Cantidad de alumnos ingresada:",cantAlu)
cont = 1
suma = 0
while cont <= cantAlu:
    cont = cont + 1
    notas = int(input("Ingresa la nota: "))
    while notas < 0 or notas > 10:
        print("Error. Nota no valida.")
        notas = int(input("Ingresa la nota: "))
    suma = suma + notas
print('\n')
promedio = suma / cantAlu
print("El promedio de los alumnos es",promedio)