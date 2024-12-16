kg = input ("¿Cuantos kg pesa?")
alt = input ("¿Cuanto mide en metros?")

q = float(kg)
w = float(alt)

# Usamos "round" para redondear el valor final de la operacion, y quitarnos algunos decimales, y para hacer una potencia debemos usar "**"

print ("Su imc es de...", round (q / (w ** 2) ) )
