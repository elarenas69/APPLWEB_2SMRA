n1 = input ("Introduzca un numero par:  ")
n2 = input ("Introduzca un numero impar:  ")


s1 = eval(n1)
s2 = eval(n2)


if s1 % 2 == 0 and s2 % 2 != 0:
    print ("Gracias por su colaboracion.")

else: 
        print ("Uno de los numeros introducidos no cumple con los requisitos"), print ("Por favor vuelva a intentarlo.")
