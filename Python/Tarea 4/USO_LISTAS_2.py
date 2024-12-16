n1 = input("Escriba un numero entero: ")
n2 = input("Escriba otro numero entero: ")

num1 = int(n1)
num2 = int(n2)

if num1 >= num2:
    print(list(range((num2 + 1), num1, 1)))

else:
    print(list(range((num1 + 1), num2, 1)))
