# FUNCIONES
def serienumerica():
    '''Crear una serie numerica en lista con numeros del 1 al 20.'''
    num = int(input("Ingresa un numero comprendido dentro del rango [1;20](-1 para finalizar): "))
    while num == 0 or num > 20 or num < -1:
        num = int(input("El numero no esta dentro del rango. Intente nuevamente (-1 para finalizar). "))
    lista = []
    while num != -1:
        lista.append(num)
        num = int(input("Ingresa un numero comprendido dentro del rango [1;20](-1 para finalizar): "))
        while num == 0 or num > 20 or num < -1:
            num = int(input("El numero no esta dentro del rango. Intente nuevamente (-1 para finalizar). "))
    print(lista)
    
# PROGRAMA PRINCIPAL
nro = serienumerica()