print(" ")
print("Andres Noe Gomez Garcia: Examen")
print(" ")

#Gomez Garcia Andres Noe
#Se le pide al usuario escribir sus apellidos y su nombre(s)
ap = str(input("Ingrese su apellido paterno: "))
am = str(input("Ingrese su apellido materno: "))
n1 = str(input("Ingrese su primer nombre: "))
n2 = str(input("Ingrese su segundo nombre: "))

#Imprime las variables con datos string que se declararon en las lineas 6,7,8,9
print(ap, am, n1,  n2,", Ahora se escribira en mayusculas: ", ap.upper(),am.upper(),n1.upper(),n2.upper())

#Deja un espacio entre lineas
print(" ")

#Gomez Garcia Andres Noe
#Se imprime el mensaje para pedir al usuario
print("Piense en 3 valores distintos")
#Se le pide al usuario ingresar 3 valores
A=float(input("Ingrese el primer valor: "))
B=float(input("Ingrese el segundo valor valor: "))
C=float(input("Ingrese el tercer valor: "))

#Si alguno de los valores son iguales El mensaje de alerta aparecera
if A==B:
    print("Hay valores iguales")
elif B == C:
    print("Hay valores iguales")
elif C==A:
    print("Hay valores iguales")
else:#Si ninguno de los valores es igual nos dira cual es mayor y cual es menor
    if A>B:
        print(A,"Es mayor que", B)
    else:
        print(B,"Es mayor que", A)

    if B>C:
        print(B, "Es mayor que", C)
    else:
        print(C,"Es mayor que", B)
    if C>A:
        print(C,"Es mayor que", A)
    else:
        (A,"Es mayor que", C)

print(" ")

#Gomez Garcia Andres Noe
#Se le pide al usuario que ingrese dos valores
x=float(input("Ingrese un valor: "))
y=float(input("Ingrese otro valor: "))

if x<y:#Si X es menor que y 
    print(x,"Es menor que", y)#Imprimira
else:#Si no se cumple la primera condicion
    print(y,"Es menor que ", x)#Imprimira
print(" ")

#Gomez Garcia Andres Noe
#Se le pide al usuario que ingrese el largo y ancho del rectangulo
w=float(input("Ingrese el ancho del rectangulo: "))
l=float(input("Ingrese el largo del rectangulo: "))

#Formula para sacar el area y el perimetro de un rectangulo
p = (2*l)+(2*w)
a = l*w
#Imprime el area y perimetro del rectangulo
print("El area del rectangulo es:", a)
print("El perimetro del rectangulo es:", p)
print(" ")

#Gomez Garcia Andres Noe
#Se le pide un numero al usuario
z=int(input("Ingrese un numero: "))

#Si el numero esta entre los 12 primeros imprimira
if z <= 12:
    print(z, "Se encuentra en la primera docena de numeros naturales")
else:#Si no impri,ira
    print(z,"No se encuentra en la primera docena de numeros")
print(" ")

#Gomez Garcia Andres Noe
#Se le pide un numero al usuario
n=int(input("Ingrese un numero del uno al 10: "))
if n==2:#Si el numero que es escribio el usuario es igual alguno de estos numeros
    print("El numero es par")#Imprimira que es par
elif n==4:
    print("El numero es par")
elif n==6:
    print("El numero es par")
elif n==8:
    print("El numero es par")
elif n==10:
    print("El numero es par")
else:#Si no
    print("El numero es impar")#Imprimira que es impar

print(" ")

#Gomez Garcia Andres Noe
#Se le pide al usuario un numero 
h=int(input("Ingrese un numero"))

#Formula para saber si es divisible 
r = h/7

if h>40:#Si h es mayor a cuarenta imprimira 
    print("El valor es mayor a cuarenta")
else:#Si no imprimira
    print("El valor es menor a cuarenta")
if r == float:#Sir es un dato float imprimira 
    print("El numero no es divisible entre 7")
else:#Si no imprimira
    print("El numero es divisible entre 7")

#Gomez Garcia Andres Noe
#Se declara la variable 
x=5
#imprime explicacion
print("Si x es igual a", x, "Entonces x! es")
#Formula para sacar factorial
r=5*4*3*2*1
#Imprime resultado
print (r)

