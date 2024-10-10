print(" ")
print("Gomez Garcia Andres Noe 3W 1184: practica 2")
print(" ")

# 10. Función que verifica si un carácter es una vocal (sin usar lower)
def es_vocal():
    caracter = input("Por favor, ingresa un carácter: ")
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u' or caracter == 'A' or caracter == 'E' or caracter == 'I' or caracter == 'O' or caracter == 'U':
        return True
    else:
        return False
    
print("¿Es vocal?: " + str(es_vocal()))