sueldoBasico = float(input("Ingresar el salario básico: "))
estadoCivil = input("Ingresar el estado civil. s para soltero, c para casado: ")
antiguedad = int(input("Ingresar los años de antigüedad: "))
#
if estadoCivil == 's':
    sueldoBasico = sueldoBasico + ((5 * sueldoBasico) / 100) * antiguedad
elif estadoCivil == 'c':
    sueldoBasico = sueldoBasico + ((7 * sueldoBasico) / 100) * antiguedad
#
jubilacion = (11 * sueldoBasico) / 100
obraSocial = (3 * sueldoBasico) / 100
sindicato = (3 * sueldoBasico) / 100
#
print('\n')
#
if estadoCivil == 's':
    print("Estado Civil: Soltero")
elif estadoCivil == 'c':
    print("Estado Civil: Casado")
print("Sueldo Basico            Antigüedad                   Descuentos                       Importe")
print(sueldoBasico,"                        ",antiguedad,"                                                   ",sueldoBasico)
print("                                                    ""    Jubilación                      ",jubilacion)
print("                                                    ""    Obra Social                     ",obraSocial)
print("                                                    ""    Sindicato                       ",sindicato)
print("______________________________________________________________________________________________________________________")
print("Sueldo Neto                                                                           ",sueldoBasico - jubilacion - obraSocial - sindicato)
