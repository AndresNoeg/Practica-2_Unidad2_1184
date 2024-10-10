print(" ")
print("Gomez Garcia Andres Noe 3W 1184: practica 2")
print(" ")

# 4. Función que calcula el total de una factura luego del IVA
def total_factura():
    cantidad = float(input("Por favor, ingresa la cantidad sin IVA: "))
    iva_input = input("Por favor, ingresa el porcentaje de IVA o presiona Enter para usar el 21%: ")
    if iva_input == "":
        iva = 21
    else:
        iva = float(iva_input)
    total = cantidad + (cantidad * iva / 100)
    return total

print("Total de factura: " + str(total_factura()))