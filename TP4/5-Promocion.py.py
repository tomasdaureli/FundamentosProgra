print("¡Bienvenido!")
legajo = int(input("Indica tu nro. de legajo: "))
parcial1 = int(input("Indica la nota del primer parcial: "))
parcial2 = int(input("Indica la nota del segundo parcial: "))
if parcial1 >= 7 and parcial2 >= 7:
    print("¡Felicitaciones, promocionaste la materia!")
elif parcial1 >= 4 and parcial2 >= 4:
    print("¡Felicitaciones, aprobaste la cursada! Solo resta el final.")
elif parcial1 >= 4 and parcial2 < 4 or parcial1 < 4 and parcial2 >= 4:
    print("Debes recuperar un parcial para poder pasar a la etapa final.")
elif parcial1 < 4 and parcial2 < 4:
    print("Lamentablemente has recursado la materia. Éxitos para la próxima.")