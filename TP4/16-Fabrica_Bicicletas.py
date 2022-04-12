paseo = int(input("Ingresar cuantas bicicletas de paseo quiere producir: "))
montaña = int(input("Ingresar cuantas bicicletas de montaña quiere producir: "))
cantTotal = paseo + montaña
aceroPaseo = 1.5
aceroMontaña = 2 
fabrica = 80
totalPaseo = paseo * aceroPaseo
totalMontaña = montaña * aceroMontaña
total = totalPaseo + totalMontaña
if total == 80:
    print("La cantidad de acero que hay en la fabrica es suficiente para producir",cantTotal,"biciletas. Ya no quedaran reservas de acero en la fabrica.")
elif total < 80:
    print("La cantidad de acero que hay en la fabrica es suficiente para producir",cantTotal,"biciletas. Quedan",80 - total,"kg de acero en la fabrica.")
elif total > 80:
    print("La cantidad de acero que hay en la fabrica no es suficiente para producir",cantTotal,"biciletas. Faltan",total - 80,"kg de acero.")