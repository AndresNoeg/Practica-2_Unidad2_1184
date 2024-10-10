print(" ")
print("Gomez Garcia Andres Noe 3W 1184: practica 2")
print(" ")

# 1. Función que muestra el saludo "Hey amigos!" cada vez que se le pida
def saludar():
    veces = int(input("¿Cuántas veces quieres que te salude? "))
    contador = 0
    while contador < veces:
        print("Hey amigos!")
        contador += 1

saludar()