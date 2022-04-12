def maximo(a,b):
    '''Definir el maximo entre dos numeros'''
    if a > b:
        print("El maximo es",a)
    elif a < b:
        print("El maximo es",b)
    else:
        print("Los numeros son iguales.")
    return

# PROGRAMA PRINCIPAL
num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))
resultado = maximo(num1,num2)