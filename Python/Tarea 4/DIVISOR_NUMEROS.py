num = input("Introduce un numero mayor que 0: ")

num = int(num)
l = list() 

if num > 0:
    for n in range(1, num + 1 ):
        if num % n == 0:
         list.append(n)
    print("Los divisores de " + str(num) + " son: " + str(l)) 

else:
    print("INTRODUZCA UN NUMERO MAYOR QUE CERO!!!")