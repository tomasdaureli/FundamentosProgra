edad = int(input("Ingresar edad (999 para finalizar el proceso): "))
men18 = 0
may18 = 0
sumaMen18 = 0
sumaMay18 = 0
while edad != 999:
    if edad < 0 or edad > 100:
        print("Edad no valida. Se considera válido una edad entre 0 y 100.")
        edad = int(input("Ingresar edad (999 para finalizar el proceso): "))
    if edad >= 18:
        may18 = may18 + 1
        sumaMay18 = sumaMay18 + edad
    if edad < 18:
        men18 = men18 + 1
        sumaMen18 = sumaMen18 + edad
    edad = int(input("Ingresar edad (999 para finalizar el proceso): "))
promedioMen = sumaMen18 // men18
promedioMay = sumaMay18 // may18
print("\n",may18,"son mayores de 18 años y",men18,"son menores.\n")
print("El promedio de edad de los mayores de 18 años es de",promedioMay,"años, y el de los menores es de",promedioMen,"años.")