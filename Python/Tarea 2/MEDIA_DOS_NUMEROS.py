# Para introducirle un valor a una variable usamos "input"
n = input ("Introduzca un numero")
p = input ("Introduzca otro numero") 

# Estas variables ahora mismo el programa las reconoce como texto, por lo que debemos usar float para decirle al programa
# que nos lo identifique como numero y no como texto
h = float(n)
j = float(p)



#Tenemos que añadir mas parentesis para que siga el orden de las operaciones.
print ("La media aritmetica de", h, "y", j, "es..", (h + j )/2  )