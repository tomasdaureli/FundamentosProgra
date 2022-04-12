nombre = input("Nombre: ")
print("Bienvenido ", nombre, "!")

nota1 = int(input("Nota primer parcial: "))
nota2 = int(input("Nota segundo parcial: "))

promedio = (nota1 + nota2) / 2

promedio = round(promedio,2)

print("Tu promedio es de ", promedio)