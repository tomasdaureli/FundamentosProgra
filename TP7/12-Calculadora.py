# FUNCIONES
def calculadora(texto):
    """Calculadora"""
    if texto == "f" or texto == "F":
        salir = "f"
        return salir
    if texto == "S" or texto == "s":
        num1 = float(input("Ingresa un numero: "))
        num2 = float(input("Ingresa otro numero: "))
        resultado = num1 + num2
        return resultado
    if texto == "R" or texto == "r":
        num1 = float(input("Ingresa un numero: "))
        num2 = float(input("Ingresa otro numero: "))
        resultado = num1 - num2
        return resultado
    if texto == 'M' or texto == 'm':
        num1 = float(input("Ingresa un numero: "))
        num2 = float(input("Ingresa otro numero: "))
        resultado = num1 * num2
        return resultado
    if texto == 'D' or texto == 'd':
        num1 = float(input("Ingresa un numero: "))
        num2 = float(input("Ingresa otro numero: "))
        resultado = num1 / num2
        return resultado

# PROGRAMA PRINCIPAL
#   CALCULADORA
#       MENU
print("___________")
print("CALCULADORA")
print('___________')
print("   MENU")
opcion = "a"
while opcion != "f" and opcion != "F":
    print("SUMA: Presiona S")
    print("RESTA: Presiona R")
    print("MULTIPLICAR: Presiona M")
    print("DIVIDIR: Presiona D")
    print("Para salir presiona F")
    opcion = calculadora(input("Elija una opcion: "))
    if opcion != "f" or opcion != "F":
        print(opcion)
print("Programa finalizado.")