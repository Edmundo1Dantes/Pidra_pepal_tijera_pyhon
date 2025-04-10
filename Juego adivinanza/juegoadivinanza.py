

import random


numero_secreto = random.randint(1,100)
adivinado = False
cant_intentos= 0
intentos = 5


print("bienvenido al juego de adivina el nuemro sereto")

while not adivinado:
    if cant_intentos >= intentos:
        print("GAME OVER")
        break

    numero = int(input("introduce un numero del 1 al 99: ") )

    if numero == numero_secreto:
        print("Feliecidades has adivinado el numero secreto")
        adivinado= True
    elif numero < numero_secreto:
        print("El numero es mayor al ingresado")
    else:
        print("El numero es menor al ingresado")

    cant_intentos += 1
