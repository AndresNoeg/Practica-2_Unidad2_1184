print(" ")
print("Gomez Garcia Andres Noe 3W 1184: practica 2")
print(" ")

# 8. Función que devuelve el mayor de tres números
def mayor():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    c = int(input("Ingresa el tercer número: "))
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    

print("Mayor de tres números: " + str(mayor()))