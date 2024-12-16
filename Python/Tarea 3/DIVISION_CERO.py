a1 = int(input("Introduzca el dividendo"))
a2 = int(input("Introduzca el divisor"))


if a2 == 0:
    print ("No se puede dividir entre cero") 

elif a1 % a2 == 0:
    print ("La division es exacta. Cociente: ", a1//a2)
else: 
    print ("La division no es exacta. Cociente: ", a1//a2, "Resto: ", a1 % a2)

