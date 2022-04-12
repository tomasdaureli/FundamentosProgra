# ENTRADAS
# legajo del empleado, salario basico, horas adicionales trabajadas, valor de las horas adicionales
# SALIDAS
# sueldo de cada empleado,sueldo promedio, cant. de empleados con sueldo superior al basico
# Se busca visualizar la cantidad de empleados de una empresa y calcular su salario, el promedio de los sueldos en general
# y ver cuantos empleados ganan mas que el basico.
print("Bienvenido\n")
legajo = int(input("Indique el legajo del empleado(-1 para finalizar): "))
while legajo < -1:
    print("Error. Vuelva a ingresar el legajo.")
    legajo = int(input("Indique el legajo del empleado(-1 para finalizar): "))
cantEmp = 0
sueldo = 0
sumaSueldo = 0
sueldoMayor = 0
while legajo != -1:
    salarioBase = int(input("Indique el salario basico del empleado: $"))
    horasAd = int(input("Indique cuantas horas adicionales trabaja el empleado: "))
    if horasAd > 0:
        valorAd = int(input("Indique el valor de la hora adicional: $"))
        sueldo = salarioBase + (horasAd * valorAd)
    else:
        sueldo = salarioBase
    if sueldo > salarioBase:
        sueldoMayor = sueldoMayor + 1
    sumaSueldo = sumaSueldo + sueldo
    cantEmp = cantEmp + 1
    print("Empleado.",legajo,"su sueldo es",sueldo)
    legajo = int(input("Indique el legajo del empleado(-1 para finalizar): "))
    while legajo < -1:
        print("Error. Vuelva a ingresar el legajo.")
        legajo = int(input("Indique el legajo del empleado(-1 para finalizar): "))
if cantEmp > 0:
    promedio = sumaSueldo / cantEmp
    print("\nEl sueldo promedio es $",promedio)
if sueldoMayor > 0:
    print(sueldoMayor,"empleado/s tienen un sueldo superior al basico.")
print("\n_______________")
print("Fin del proceso.")