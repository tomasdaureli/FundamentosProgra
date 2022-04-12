efectivo = int(input("Indique la cantidad de efectivo que desea retirar: "))
print("Aquí tienes")
mil = efectivo // 1000
print(mil," billetes de $1000")
quini = efectivo % 1000
b500 = quini // 500
print(b500," billetes de $500")
dosc = quini % 500
b200 = dosc // 200
print(b200," billetes de $200")
cien = dosc % 200
b100 = cien // 100
print(b100," billetes de $100")
cincu = cien % 100
b50 = cincu // 50
print(b50," billetes de $50")
veinte = cincu % 50
b20 = veinte // 20
print(b20," billetes de $20")
diez = veinte % 20
m10 = diez // 10
print(m10," monedas de $10")
cinco = diez % 10
m5 = cinco // 5
print(m5," monedas de $5")
dos = cinco % 5
m2 = dos // 2
print(m2," monedas de $2")
uno = dos % 2
m1 = uno // 1
print(m1," monedas de $1")
