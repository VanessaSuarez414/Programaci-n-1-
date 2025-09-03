#Operadores Logicos
#AND
num1 = 5
num2 = 10
print(num1 < 10 and num2 > 5) # 1 1 = 1
print(num1 < 10 and num2 < 5) # 1 0 = 0
print(num1 > 10 and num2 > 5) # 0 1 = 0
print(num1 > 10 and num2 <5)  # 0 0 = 0

#Inicio se sesion
usuario ="angiesuarez"
contraseña =1234
#Solicitar nombre usuario  y contraseña
input_contaseña = input("Ingrese su nombre de usuario:")
input_contraseña = input(input("Ingrese su contraseña: "))
#print(input_usuario == usuario and input_contraseña == contraseña)

#OR
print(num1 < 10 or num2 > 5 ) # 1 1 = 1
print(num1 < 10 or num2 < 5) # 1 0 = 0
print(num1 > 10 or num2 > 5) # 0 1 = 0
print(num1 > 10 or num2 <5)  # 0 0 = 0

#NOT
print(not(num1 < 10)) #not(1) = 0
print(not(num1 > 10)) #not(0) = 1


