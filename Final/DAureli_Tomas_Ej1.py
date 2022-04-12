# ENTRADAS
# Numeros enteros (-1 para finalizar).
# SALIDAS
# Mayor numero y la suma de sus digitos.

num = int(input("Ingrese un numero entero (-1 para finalizar): "))
mayor = 0
sumaDig = 0
while num != -1:
    if num > mayor:
        mayor = num
        sumaDig = 0
        while num != 0:
            dig = num % 10
            sumaDig = sumaDig + dig
            num = num // 10
    num = int(input("Ingrese un numero entero (-1 para finalizar): "))
print("El mayor numero ingresado fue: ", mayor)
print("La suma de sus digitos da como resultado : ",sumaDig)