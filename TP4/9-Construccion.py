# Hecho en base a un plano propio
print("AMBIENTE")
ambienteLargo = float(input("Ingresa el largo del ambiente en metros: "))
ambienteAncho = float(input("Ingresa el ancho del ambiente en metros: "))
ambienteAltura = float(input("Ingresa la altura del ambiente en metros: "))
print('\n')
print("PUERTA")
puertaAltura = float(input("Ingresa la altura de la puerta en metros: "))
puertaAncho = float(input("Ingresa el ancho de la puerta en metros: "))
puerta = puertaAltura * puertaAncho
print('\n')
print("VENTANA")
ventanaAltura = float(input("Ingresa la altura de la ventana en metros: "))
ventanaAncho = float(input("Ingresa el ancho de la ventana en metros: "))
ventana = ventanaAltura * ventanaAncho
print('\n')
print("CERAMICA")
ceramicaLargo = float(input("Ingresar la medida de un lado de la ceramica en metros: "))
ceramicaAlto = float(input("Ingresar la medida del otro lado de la ceramica en metros: "))
ceramica = ceramicaLargo * ceramicaAlto
costo = float(input("Ingresar el costo del paquete de ceramicas: $"))
cantidad = int(input("Ingresar la cantidad de ceramicas que vienen por paquete: "))
#paredes
pared1 = ambienteAncho * ambienteAltura
pared2 = (ambienteLargo * ambienteAltura) - puerta
pared3 = ambienteAncho * ambienteAltura
pared4 = (ambienteLargo * ambienteAltura) - ventana
#calculos
pc1 = pared1 / ceramica
pc2 = pared2 / ceramica
pc3 = pared3 / ceramica
pc4 = pared4 / ceramica
total = pc1 + pc2 + pc3 + pc4
print('\n')
#primera impresion
print("El ambiente requerirá",total,"cerámicas.")
print("El costo total de ceramicas será de $",(total / cantidad) * costo)
#pueden agregarse condicionales para demostrar que no es valido un dato ingresado. ej. una medida en valor negativo