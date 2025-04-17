## Problematica: Que ingrese la edad y si es mayor de 18 puede ingresar, si es menor no puede ingresar 

Edad = int(input("Por favor ingresa tu edad: "))

if Edad >= 18:
    print("Puedes ingresar")
elif Edad < 18:
    print("No puedes ingresar")