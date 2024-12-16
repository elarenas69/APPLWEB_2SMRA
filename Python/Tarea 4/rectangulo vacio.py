# Pedir al usuario el alto y el ancho del rectángulo
alto = int(input("Introduzca el alto: "))
ancho = int(input("Introduzca el ancho: "))

# Bucle para crear el rectángulo con bordes de asteriscos
for i in range(alto):
    linea = ""  # Variable para construir cada línea
    for j in range(ancho):
        # Pintar asterisco si es el borde superior, inferior, izquierdo o derecho
        if i == 0 or i == alto - 1 or j == 0 or j == ancho - 1:
            linea += "*"
        else:
            linea += " "
    print(linea)  # Imprimir la línea completa

