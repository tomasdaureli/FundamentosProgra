nombres = ["Juan", "Pablo", "Damián", "Manuel", "Nahuel", "Lucas"]
edades = [ 28, 22, 12, 18, 25, 43 ]
print(nombres)
print(edades)
i = 0
ordenado = False
while ordenado == False:
    ordenado = True
    for i in range(len(edades)-1):
        for j in range(i+1,len(edades)):
            if edades[i] < edades[j]:
                auxE = edades[j]
                auxN = nombres[j]
                edades[j] = edades[i]
                nombres[j] = nombres[i]
                edades[i] = auxE
                nombres[i] = auxN
                ordenado = False
            i = i + 1
            j = j + 1
print(nombres)
print(edades)