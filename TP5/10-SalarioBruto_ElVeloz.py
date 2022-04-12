print("________")
print("El Veloz")
print("\n")
nombre = input("Nombre del vendedor: ")
salario = float(input("Salario base mensual: "))
unidades = int(input("Cantidad de unidades vendidas: "))
cont = 0
suma = 0
while cont != unidades:
    precio = float(input("Precio de cada unidad: $"))
    comision = precio * 0.015
    suma = suma + comision
    cont = cont + 1
print(nombre,"ha vendido",unidades,"auto/s este mes, por lo que su salario es",salario + suma)
    