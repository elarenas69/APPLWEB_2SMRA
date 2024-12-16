# Usando el modulo "%" podria haberme ahorrado pasos, ya que con este podria haber sacado el resto del tiron sin tener que hacer operaciones adicionales.

seg = input ("Introduce una cantidad de segundos..")

w = int(seg)

x = (w // 60) 

s = x // 60

e = x - (s *60 )

o = (w - (e * 60)) + (w - ((s *60 ) *60) )

a = (o - w )

print (seg,"segundos son", s, "horas", e,"minutos y ", a, "segundos" )
