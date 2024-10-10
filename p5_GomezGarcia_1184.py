print(" ")
print("Gomez Garcia Andres Noe 3W 1184: practica 2")
print(" ")

# 5. Funciones para calcular el área de un círculo y el volumen de un cilindro
import math

def area_circulo():
    radio = float(input("Por favor, ingresa el radio del círculo: "))
    return math.pi * radio * radio

def vol_cilindro():
    radio = float(input("Por favor, ingresa el radio del cilindro: "))
    altura = float(input("Por favor, ingresa la altura del cilindro: "))
    return area_circulo() * altura

print("Área de un círculo: " + str(area_circulo()))

print("Volumen de un cilindro: " + str(vol_cilindro()))