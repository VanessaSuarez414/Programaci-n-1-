#Calculo Volumen pelota

#Entradas
radio = float(input("Ingrese el radio de la pelota (en cm): "))

pi = 3.14159

if radio > 0:
     Volumen = (4/3) * pi * (radio ** 3)
     print("El volumen de la pelotae es:", Volumen, "cm³")
elif radio == 0:
     print("El volumen es 0 porque el radio es 0")
else:
     print("Error: el radio de la pelota no puede ser negativo")
   