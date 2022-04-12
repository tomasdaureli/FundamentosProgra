user = input("Usuario: ")
password = input("Contraseña: ")
intentos = 1
while user != "admin" and password != 1234:
    if intentos < 3:
        print("Usuario y/o contraseña incorrectos.")
        user = input("Usuario: ")
        password = input("Contraseña: ")
        intentos = intentos + 1
    else:
        print("Se acabaron los intentos.")
print("Login exitoso.")
        
