import math

# Solicitar entradas del usuario
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

dx = x2 - x1
dy = y2 - y1


a = math.sin(dx / 2)**2 + math.cos(x1) * math.cos(x2) * math.sin(dy / 2)**2
c = 2 * math.asin(math.sqrt(a))

distance = 6371.01 * c
distanceR= round(distance)

print(distanceR)


#Problema1
n1= float(input("Numero 1:"))
n2= float(input("Numero 2:"))
r= n1+n2 
print("el resultado es", r)