terms = int(input("Indique la cantidad de terminos: "))
while terms < 0:
    print("Error")
    terms = int(input("Indique la cantidad de terminos: "))
exp = 0
suma = 0
cont = 0
print("Serie:")
while cont != terms:
    num = 1 / 2 ** exp
    print(num)
    exp = exp + 1
    suma = suma + num
    cont = cont + 1
promedio = suma / terms
print("El promedio de los terminos generados es",promedio)