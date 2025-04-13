

nombre1 = input("Cómo se llamará el jugador 1:")
nombre2 = input("Cómo se llamará el jugador 2:")


Intentos = 0
Victorias_j1_ = 0
Victorias_j2_ = 0
NPG = 2


while Victorias_j1_ < 2 and Victorias_j2_<2 and Intentos < 5:
    
    jugador1 = input("Hola "+ nombre1 + " Que eliges, piedra papel o tijera: ")
    jugador2 = input("Hola "+ nombre2 + " Que eliges, piedra papel o tijera: ")


    j1 = jugador1.casefold()
    j2 = jugador2.casefold()


    Condicion1 = j1 == "piedra" and j2 == "tijera"
    Condicion2 = j1 == "papel" and j2 == "piedra" 
    Condicion3 = j1 == "tijera" and j2 == "papel"
    

    if j1 == j2 :
        print("Ha sido un empate")
    elif (Condicion1) or (Condicion2) or (Condicion3):
        print("Ha ganadado", nombre1)
        Victorias_j1_ += 1
    else: 
        print("Ha ganado", nombre2)
        Victorias_j2_ += 1
    Intentos += 1 


if Victorias_j1_ >= NPG:
    print("🎉 ¡Ganador final:", nombre1, "!")
elif Victorias_j2_ >= NPG:
    print("🎉 ¡Ganador final:", nombre2, "!")
else:
    print("¡Empate final!")
    