# FUNCIONES
def milista():
    '''Crear una lista con numeros ingresados desde el teclado ordenada de forma ascendente.'''
    lista = []
    ant = 0
    num = 0
    while num != -1:
        num = int(input("Ingresa un numero positivo(-1 para finalizar): "))
        while num < -1:
            num = int(input("Error. Ingresa un numero positivo(-1 para finalizar): "))
        if num >= ant:
            lista.append(num)
        else:
            while num < ant and num != -1:
                num = int(input("Error. Ingresa un numero positivo(-1 para finalizar): "))
                if num >= ant:
                    lista.append(num)
        ant = num
    return lista

def orden(lista,num):
    '''Ordenar el ultimo numero ingresado en la lista.'''
    i = len(lista)-2
    ult = len(lista)-1
    listo = False
    while listo == False:
        listo = True
        if lista[i] < num:
                aux = lista[i]
                lista[i] = lista[ult]
                lista[ult] = aux
                listo = False
    return lista    

# PROGRAMA PRINCIPAL
nro = milista()
print(nro)
nuevo = int(input("Ingrese un nuevo numero para incorporar a la lista: "))
nro.append(nuevo)
ordenado = orden(nro,nuevo)
print(nro)

# Sin resolver parte de agregar numero.