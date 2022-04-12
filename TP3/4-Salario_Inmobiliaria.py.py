print("¡Bienvenido!")
vendedor = int(input("Ingresa el numero de vendedor: "))
salario = int(input("Ingresa el salario del vendedor: $"))
ventas = int(input("Ingresa el total de las ventas realizadas por el vendedor este mes: "))
valorVenta = int(input("Ingresa el valor total de las ventas realizadas: $"))
comision = ((salario * 15) / 100) * ventas
comisionVenta = (valorVenta * 5) / 100
print("El vendedor nº",vendedor,"cobrará un salario de $",salario + comision + comisionVenta," este mes.")