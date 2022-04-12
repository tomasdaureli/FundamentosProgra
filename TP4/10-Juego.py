print("¡HORA DE JUGAR!\nBienvenido, el juego consiste en responder 3 preguntas correctamente,\nsi se responde mal alguna de las preguntas no se formulara la siguiente\ny el juego se dara por terminado.")
preg1 = input("¿2 + 2 es 5? ")
if preg1 == 'no' or preg1 == 'No' or preg1 == 'NO' or preg1 == 'nO':
    print("¡Correcto!")
    preg2 = input("¿5 + 5 es 10? ")
    if preg2 == 'si' or preg2 == 'Si' or preg2 == 'SI' or preg2 == 'sI':
        print("¡Correcto!")
        preg3 = input("¿22hs es lo mismo que 10pm? ")
        if preg3 == 'si' or preg3 == 'Si' or preg3 == 'SI' or preg3 == 'sI':
            print("¡Correcto! Has ganado el juego. Felicitaciones.")
        else:
            print("Incorrecto. Has perdido el juego. Buena suerte la proxima vez.")
    else:
        print("Incorrecto. Has perdido el juego. Buena suerte la proxima vez.")
        
else:
    print("Incorrecto. Has perdido el juego. Buena suerte la proxima vez.")
    