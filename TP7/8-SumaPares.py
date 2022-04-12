# FUNCION
def par_impar(a):
    num = bool(a % 2 == 0)
    print(num)
    return

# PROGRAMA PRINCIPAL (faltaria validacion de numero positivo)
num = int(input("Numero: "))
suma = 0
cont = 0
while num != -1:
    vof = par_impar(num)
    if num % 2 == 0:
        suma = suma + num
        cont = cont + 1
    num = int(input("Numero: "))
print("Se ingresaron un total de",cont,"numero/s par/es, y la suma total de los pares es",suma)
print("El programa ha finalizado.")