# Definir el tamaño del cuadrado
tamaño = int(input("Introduzca un tamaño del cuadrado"))

# Bucle para crear el cuadrado con bordes de asteriscos
for i in range(tamaño):
    for j in range(tamaño):
        # Pintar asterisco si es el borde superior, inferior, izquierdo o derecho
        if i == 0 or i == tamaño - 1 or j == 0 or j == tamaño - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # Salto de línea después de cada fila
