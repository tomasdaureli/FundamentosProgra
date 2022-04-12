num = int(input("Ingrese un numero entero (0 para terminar): "))
maximo = 0
minimo = num
suma = 0
cont = 1
while num != 0:
    if num > maximo:
        maximo = num
    if num < minimo:
        minimo = num
    suma = suma + num
    cont = cont + 1
    num = int(input("Ingrese un numero entero (0 para terminar): "))
promedio = suma / cont
print("El promedio de los numeros ingresados es",promedio)
print("El maximo numero ingresado fue",maximo)
print("El minimo numero ingresado fue",minimo)