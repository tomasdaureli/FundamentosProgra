hermano1 = input("Indica el nombre del primer niño: ")
hermano2 = input("Indica el nombre del segundo niño: ")
edad1 = int(input("Indica la edad del primer niño: "))
edad2 = int(input("Indica la edad del segundo niño: "))
if edad1 > edad2:
    print(hermano1,"es mayor que",hermano2)
elif edad2 > edad1:
    print(hermano2,"es mayor que",hermano1)
elif edad1 == edad2:
    print(hermano1, "y",hermano2,"son mellizos.")
    