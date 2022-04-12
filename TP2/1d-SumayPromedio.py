#d 
print("Ingresar 3 numeros para realizar el promedio ")
numero1 = int(input("Dime el primer numero: "))
numero2 = int(input("Dime el segundo numero: "))
numero3 = int(input("Dime el tercer numero: "))
suma = numero1 + numero2 + numero3
print("La suma es ",suma)
promedio = round(suma / 3,2)
print("Y el promedio es ", promedio)