print(" ")
print("Gomez Garcia Andres Noe 3W 1184: practica 2")
print(" ")

# 3. Función que calcula el factorial de un número entero positivo
def fac():
    n = int(input("Por favor, ingresa un número entero positivo para calcular su factorial: "))
    if n < 0:
        return "El número debe ser positivo."
    resultado = 1
    contador = 1
    while contador <= n:
        resultado = resultado * contador
        contador = contador + 1
    return resultado

print("Factorial: " + str(fac()))