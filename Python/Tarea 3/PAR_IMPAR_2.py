n1 = input ("Introduzca un numero par:  ")


s1 = eval(n1)


if s1 % 2 == 0:
    n2 =eval(input("Introduzca un numero impar: "))
    
    if n2 % 2 == 1 :
     
        print ("Gracias por su colaboración")
   
    else: 
        print ("El numero introducido no es impar, por favor introduzca otro numero") 

else:  
    print ("El numero introducido no es par, por favor introduzca otro numero")