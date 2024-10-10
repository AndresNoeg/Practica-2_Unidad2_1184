print(" ")
print("Gomez Garcia Andres Noe 3W 1184: practica 2")
print(" ")

# 7. Función que regresa la longitud de la última palabra en un string
def longitud_ultima_palabra():
    frase = input("Por favor, ingresa una frase: ")
    palabras = frase.split()
    ultima_palabra = palabras[len(palabras) - 1]
    contador = 0
    for letra in ultima_palabra:
        contador = contador + 1
    return contador

print("Longitud de la última palabra: " + str(longitud_ultima_palabra()))