import math
numero = int(input("Introduce un número natural entre 100 y 999: "))
centenas = numero // 100
decenas = (numero % 100) // 10
unidades = numero % 10
print(f"Centenas: {centenas}, Decenas: {decenas}, Unidades: {unidades}")
letra = input("Introduce una letra: ")
num = int(input("Introduce un número de repeticiones: "))
cadena = letra * num
print("La cadena es:", cadena)
numero_raiz = float(input("Introduce un número para calcular su raíz cuadrada: "))
raiz_cuadrada = math.sqrt(numero_raiz)
print(f"La raíz cuadrada de {numero_raiz} es: {raiz_cuadrada}")
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))
discriminante = b**2 - 4*a*c
if discriminante >= 0:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"Las soluciones de la ecuación son: x1 = {x1}, x2 = {x2}")
else:
    print("La ecuación no tiene soluciones reales.")
x1 = float(input("Introduce la coordenada x1: "))
y1 = float(input("Introduce la coordenada y1: "))
x2 = float(input("Introduce la coordenada x2: "))
y2 = float(input("Introduce la coordenada y2: "))
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
punto_medio_x = (x1 + x2) / 2
punto_medio_y = (y1 + y2) / 2
print(f"La distancia euclidiana entre los puntos es: {distancia}")
print(f"El punto medio es: ({punto_medio_x}, {punto_medio_y})")
