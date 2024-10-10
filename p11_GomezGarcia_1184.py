print(" ")
print("Gomez Garcia Andres Noe 3W 1184: practica 2")
print(" ")

# 11. Función que calcula la distancia dirigida entre dos puntos
def distancia_dirigida():
    x1 = float(input("Ingresa la coordenada x1: "))
    y1 = float(input("Ingresa la coordenada y1: "))
    x2 = float(input("Ingresa la coordenada x2: "))
    y2 = float(input("Ingresa la coordenada y2: "))
    distancia_x = x2 - x1
    distancia_y = y2 - y1
    return distancia_x, distancia_y

print("Distancia dirigida: " + str(distancia_dirigida()))