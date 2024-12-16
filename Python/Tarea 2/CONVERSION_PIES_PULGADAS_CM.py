pies = input ("Escriba una cantidad de pies:")
pulgadas = input ("Escriba una cantidad de pulgadas")


q = float(pies) 
w = float(pulgadas)


print ( pies, "pies y", pulgadas, "pulgadas son", (( q * 12 ) * 2.54) + (w * 2.54), "cm")