terms = int(input("Indique la cantidad de terminos que desea imprimir: "))
cont = 0
num = 1
suma = 0
print("Serie:\n")
while cont != terms:
    print(num)
    suma = suma + num
    cont = cont + 1
    num = (num * 2) + 5
print("Suma de los numeros de la serie:",suma)