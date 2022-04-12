año = int(input("Indica el año que deseas consultar: "))
if año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
    print(año,"es un año biciesto.")
elif año % 4 == 0 and año % 100 == 0:
    print(año,"no es un año biciesto.")
elif año % 4 == 0:
    print(año,"es un año biciesto.")
elif año % 4 != 0:
    print(año,"no es un año biciesto.")
    