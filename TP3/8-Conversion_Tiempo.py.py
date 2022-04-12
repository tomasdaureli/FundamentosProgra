num = int(input("Indique la cantidad de segundos que desea visualizar: "))
dias = num // 86400
diaResto = num % 86400
horas = diaResto // 3600
horaResto = diaResto % 3600
minutos = horaResto // 60
minutoResto = horaResto % 60
segundos = minutoResto
print("Son ",dias," días, ",horas," horas, ",minutos," minutos, ",segundos," segundos.")