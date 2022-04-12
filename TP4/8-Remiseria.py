km = float(input("¿Cuántos kilometros recorrerá? "))
#
if km <= 6:
    print("El costo del viaje es de $50.")
elif km > 6 and km < 10:
    print("El costo del viaje es de $",20 * km)
elif km > 10:
    print("El costo del viaje es de $",15 * km)