print(" ")
print("Gomez Garcia Andres Noe 3W 1184: practica 2")
print(" ")

# 6. Función que valida una dirección de email con input()
def validar_email():
    email = input("Por favor, ingresa tu dirección de email: ")
    if "@" in email:
        return "La dirección de email es válida."
    else:
        return "La dirección de email no es válida."
    

print(validar_email())