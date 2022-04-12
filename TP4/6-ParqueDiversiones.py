print("Bienvenido")
niño1 = input("Indica el nombre del primer niño: ")
niño2 = input("Indica el nombre del segundo niño: ")
edad1 = int(input("Indica la edad del primer niño: "))
edad2 = int(input("Indica la edad del segundo niño: "))
altura1 = float(input("Indica la altura del primer niño: "))
altura2 = float(input("Indica la altura del segundo niño: "))
# entonces
print("Los datos ingresados son los siguientes, \n")
print(niño1,"\nTiene",edad1,"años y mide ",altura1,"metros.\n")
print(niño2,"\nTiene",edad2,"años y mide ",altura2,"metros.\n")
# por lo tanto
if edad1 >= 15 and altura1 > 1.50 and edad2 >= 15 and altura2 > 1.50:
    print("Ambos pueden acceder a la montaña rusa.")
elif edad1 >= 15 and altura1 > 1.50 and edad2 >= 15 and altura2 < 1.50:
    print(niño1," puede acceder a la montaña rusa. ",niño2," no puede acceder debido a que no cumple con los requisitos.")
elif edad1 >= 15 and altura1 > 1.50 and edad2 < 15 and altura2 > 1.50:
    print(niño1," puede acceder a la montaña rusa. ",niño2," no puede acceder debido a que no cumple con los requisitos.")
elif edad1 >= 15 and altura1 < 1.50 and edad2 >= 15 and altura2 < 1.50:
    print(niño2," puede acceder a la montaña rusa. ",niño1," no puede acceder debido a que no cumple con los requisitos.")
elif edad1 < 15 and altura1 > 1.50 and edad2 >= 15 and altura2 > 1.50:
    print(niño2," puede acceder a la montaña rusa. ",niño1," no puede acceder debido a que no cumple con los requisitos.")
elif edad1 >= 15 and altura1 > 1.50 and edad2 < 15 and altura2 < 1.50:
    print(niño1," puede acceder a la montaña rusa. ",niño2," no puede acceder debido a que no cumple con los requisitos.")
elif edad1 < 15 and altura1 < 1.50 and edad2 >= 15 and altura2 > 1.50:
    print(niño2," puede acceder a la montaña rusa. ",niño1," no puede acceder debido a que no cumple con los requisitos.")
elif edad1 >= 15 and altura1 < 1.50 and edad2 >= 15 and altura2 < 1.50:
    print("Ninguno de los dos niños puede acceder a la montaña rusa debido a que no cumplen con los requisitos.")
elif edad1 < 15 and altura1 > 1.50 and edad2 < 15 and altura2 > 1.50:
    print("Ninguno de los dos niños puede acceder a la montaña rusa debido a que no cumplen con los requisitos.")
elif edad1 < 15 and altura1 < 1.50 and edad2 < 15 and altura2 < 1.50:
    print("Ninguno de los dos niños puede acceder a la montaña rusa debido a que no cumplen con los requisitos.")