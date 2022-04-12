# FUNCIONES
def tituloAsteriscos(texto,a):
    '''Imprimir una fila de asteriscos sobre el titulo'''
    titulo = texto
    cont = 0
    while cont != a:
        print("*",end="")
        cont = cont + 1
    print("\n",titulo,)
    cont = 0
    while cont != a:
        print("*",end="")
        cont = cont + 1
    
    
# PROGRAMA PRINCIPAL
titulo = input("Ingresa tu titulo: ")
asteriscos = int(input("Ingresa la longitud de asteriscos que deseas: "))
resultado = tituloAsteriscos(titulo,asteriscos)