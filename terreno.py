#Solicitar datos del terreno
base = float(input("Ingrese la base del terreno en metros cuadrados:  "))
altura = float(input("Ingrese la altura del terreno en metros:  "))
#Calcular el area del terreno
Area_triangulo = ( base * altura ) / 2
Area_cuadrado = base * altura
Area_total = Area_triangulo + Area_cuadrado
#Precio del terreno
Precio_metro_cuadrado = 440000
Precio_total_terreno = Area_total * Precio_metro_cuadrado
#Mostrar la informacion
print(f"El area total del terreno es:{Area_total}mts2")
print(f"El precio total del terrerno es: ${Precio_total_terreno} COP")