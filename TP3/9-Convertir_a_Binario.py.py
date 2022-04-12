numbin = int(input("Ingresa un numero binario de 4 cifras para convertirlo: "))
dig0 = numbin % 10
numbin = numbin // 10
dig1 = numbin % 10
numbin = numbin // 10
dig2 = numbin % 10
numbin = numbin // 10
dig3 = numbin % 10
numbin = numbin // 10
numdec = (dig0 * 2 ** 0 + dig1 * 2 ** 1 + dig2 * 2 ** 2 + dig3 * 2 ** 3)
print("Tu numero decimal es ",numdec,".")