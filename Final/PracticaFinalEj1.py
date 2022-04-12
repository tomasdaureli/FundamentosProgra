n = int(input("Ingrese un numero entero, positivo y menor que 100: "))
while n >= 100:
    print("Error. El numero debe ser menor que 100.")
    n = int(input("Ingrese un numero entero, positivo y menor que 100: "))
cont = 1
suma = 0
print("Divisores:",end=" ")
while cont < n:
    if n % cont == 0:
        print(cont, end=" ")
        suma = suma + cont
    cont = cont + 1
print("\n")
if suma > n:
    print(n, " es numero abundante.")
elif suma < n:
    print(n, " es numero deficiente.")
else:
    print(n, " es numero perfecto.")