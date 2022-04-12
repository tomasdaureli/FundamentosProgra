print("======================================")
print("Veamos en que fecha se realiza Pascua.")
print("======================================")
print('\n')
año = int(input("Ingresar el año: "))
print('\n')
#formulas
a = año % 19
b = año % 4
c = año % 7
d = ((a * 19) + 24) % 30
e = ((b * 2) + (c * 4) + (d * 6) + 5) % 7
pascua = d + e + 22
#resultado
if pascua > 31:
    print("En",año,"Pascua se realiza el",pascua - 31,"de abril.")
else: 
    print("En",año,"Pascua se realiza el",pascua,"de marzo.")

