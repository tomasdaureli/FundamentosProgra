dia = int(input("Ingresa el día: "))
mes = int(input("Ingresa el mes: "))
año = int(input("Ingresa el año: "))
print('\n')
if año > 1 and mes == 2 and dia <= 28:
    print("La fecha ",dia,"/",mes,"/",año," es válida.")
elif año > 1 and año % 4 == 0  and mes == 2 and dia <= 29 or año % 4 == 0 and año % 100 == 0 and año % 400 == 0 and mes == 2 and dia <= 29:
    print("La fecha ",dia,"/",mes,"/",año," es válida.")
elif año > 1 and mes == 1 and dia <= 31:
    print("La fecha",dia,"/",mes,"/",año,"es válida.")
elif año > 1 and mes == 3 and dia <= 31:
    print("La fecha ",dia,"/",mes,"/",año," es válida.")
elif año > 1 and mes == 5 and dia <= 31:
    print("La fecha ",dia,"/",mes,"/",año," es válida.")
elif año > 1 and mes == 7 and dia <= 31:
    print("La fecha ",dia,"/",mes,"/",año," es válida.")
elif año > 1 and mes == 8 and dia <= 31:
    print("La fecha ",dia,"/",mes,"/",año," es válida.")
elif año > 1 and mes == 10 and dia <= 31:
    print("La fecha ",dia,"/",mes,"/",año," es válida.")
elif año > 1 and mes == 12 and dia <= 31:
    print("La fecha ",dia,"/",mes,"/",año," es válida.")
elif año > 1 and mes == 4 and dia <= 30:
    print("La fecha ",dia,"/",mes,"/",año," es válida.")
elif año > 1 and mes == 6 and dia <= 30:
    print("La fecha ",dia,"/",mes,"/",año," es válida.")
elif año > 1 and mes == 9 and dia <= 30:
    print("La fecha ",dia,"/",mes,"/",año," es válida.")
elif año > 1 and mes == 11 and dia <= 30:
    print("La fecha ",dia,"/",mes,"/",año," es válida.")
else:
    print("La fecha ",dia,"/",mes,"/",año," no es válida.")
# agregar que los dias y los meses deben ser mayores a 1. para no guardar valores negativos en la variable.
    