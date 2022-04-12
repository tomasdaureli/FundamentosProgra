num = int(input("Ingresa un numero: "))
sumaPar = 0
cont = 1
while sumaPar < 100:
    if num % 2 == 0:
        sumaPar = sumaPar + num
    cont = cont + 1
    num = int(input("Ingresa un numero: "))
print("Se han ingresado",cont,"numeros.")