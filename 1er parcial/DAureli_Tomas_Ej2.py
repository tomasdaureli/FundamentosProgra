# ENTRADAS
# numeros al azar
# SALIDAS
# cantidad de numeros impares, mayor cantidad de numeros pares ingresados de forma consecutiva
# Se ingresaran por teclado numeros al azar y se buscara identificar cuantos de ellos fueron impares
# y cual fue la mayor cantidad de numeros pares que fueron ingresados de forma consecutiva
num = int(input("Ingresa un numero al azar(-1 para finalizar): "))
anterior = 0
cont = 0
consecutivo = 0
impares = 0 
while num != -1:
    if num % 2 != 0:
        impares = impares + 1
    if num % 2 == 0:
        anterior = num
        cont = cont + 1
        if cont > consecutivo:
            consecutivo = cont
    else:
        cont = 0
    num = int(input("Ingresa un numero al azar(-1 para finalizar): "))
print("Cantidad de numeros impares:",impares)
print("Mayor cantidad de numeros pares ingresados de forma consecutiva:",consecutivo)
        