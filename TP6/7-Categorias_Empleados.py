legajo = int(input("Nro. de legajo (0 para terminar): "))
total = 0
mas20 = 0
menos5 = 0
mayor = 0
mayorLegajo = 0
totalA = 0
totalB = 0
totalC = 0
empleados = 1
menor = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
while legajo != 0:
    while legajo < 0 or legajo == "":
        print("Error. Ingrese nuevamente el nro. de legajo.")
        legajo = int(input("Nro. de legajo (Fin para terminar): "))
    categoria = str(input("Categoria: "))
    validez = 0
    while validez != 1:
        if categoria == "a":
            validez = 1
        elif categoria == "A":
            validez = 1
        elif categoria == "b":
            validez = 1
        elif categoria == "B":
            validez = 1
        elif categoria == "c":
            validez = 1
        elif categoria == "C":
            validez = 1
        else:
            print("Error. Ingrese nuevamente la categoria.")
            categoria = input("Categoria: ")
            validez = 0
    salario = int(input("Salario: "))
    total = total + salario
    suma = 0
    while salario < 0:
        print("Error. Ingrese nuevamente el salario.")
        salario = int(input("Salario: "))
    if salario > 20000:
        mas20 = mas20 + 1
    if categoria == "c" and salario < 5000:
        menos5 = menos5 + 1
    elif categoria == "C" and salario < 5000:
        menos5 = menos5 + 1
    if mayor < salario:
        mayor = salario
        mayorLegajo = legajo
    if menor > salario:
        menor = salario
    if categoria == "a":
        totalA = totalA + salario
    elif categoria == "A":
        totalA = totalA + salario
    elif categoria == "b":
        totalB = totalB + salario
    elif categoria == "B":
        totalB = totalB + salario
    elif categoria == "c":
        totalC = totalC + salario
    elif categoria == "C":
        totalC = totalC + salario
    legajo = int(input("Nro. de legajo (0 para terminar): "))
    empleados = empleados + 1 
promedio = total / empleados
print("_______")
print("INFORME",
      "\n- Importe total de salarios pagados por la empresa. $",total,
      "\n- Cantidad de empleados que ganan más de $20000. ",mas20,
      "\n- Cantidad de empleados que ganan menos de $5000, cuya categoría sea “C”. ",menos5,
      "\n- Legajo del empleado que más gana. ",mayorLegajo,
      "\n- Sueldo más bajo. ",menor,
      "\n- Importe total de sueldos por cada categoría.",
      "\n  ~ Cat. A: $",totalA,
      "\n  ~ Cat. B: $",totalB,
      "\n  ~ Cat. C: $",totalC,
      "\n- Salario promedio. $",promedio)