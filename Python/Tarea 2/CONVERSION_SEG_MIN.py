

seg = input ("Introduce una cantidad de segundos..")

w = int(seg)

q = (w / 60) 

e = int(q)

z = ((w / 60) - e ) * 60
12
t = int(z)

print (seg, "segundos son", e, "minutos y ", round (z ), "segundos" )