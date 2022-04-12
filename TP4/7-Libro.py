paginas = int(input("¿Cuántas páginas tiene tu libro? "))
#
if paginas < 300:
    print("El costo aproximado del libro es de $",125 + (2.20 * paginas))
elif paginas > 300:
    print("El costo aproximado del libro es de $",125 + (2.20 * paginas) + 80)
elif paginas > 600:
    print("El costo aproximado del libro es de $",125 + (2.20 * paginas) + 80 + 136)
    