##Resolver el problema de devolver el area del circulo cuando nos dan el radio




import math


radio = float(input("Por favor ingresa el radio del circulo y asi te devolvere el area del mismo: "))
pi = math.pi
radio_cuadradro = radio**2
Area = pi*radio_cuadradro

print("El area del circulo con radio", radio, "es", Area)