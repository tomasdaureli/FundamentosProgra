listaA = []
listaB = []
listaC = []
for lista in range(5):
    numA = int(input("Ingrese un numero para la lista A: "))
    listaA.append(numA)
    numB = int(input("Ingrese un numero para la lista B: "))
    listaB.append(numB)
    listaC.append(numA + numB)
print('\n')
print(listaA,end=" y ")
print(listaB,end=" → ")
print(listaC)