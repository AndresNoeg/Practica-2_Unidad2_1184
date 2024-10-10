print(" ")
print("Gomez Garcia Andres Noe 3W 1184: practica 2")
print(" ")

# 9. Funciones para sumar y multiplicar los números de una lista
def suma():
    lista = input("Ingresa los números separados por espacios: ").split()
    lista = [int(num) for num in lista]
    resultado = 0
    contador = 0
    while contador < len(lista):
        resultado = resultado + lista[contador]
        contador = contador + 1
    return resultado

def multip():
    lista = input("Ingresa los números separados por espacios: ").split()
    lista = [int(num) for num in lista]
    resultado = 1
    contador = 0
    while contador < len(lista):
        resultado = resultado * lista[contador]
        contador = contador + 1
    return resultado

print("Suma de la lista: " + str(suma()))
print("Multiplicación de la lista: " + str(multip()))