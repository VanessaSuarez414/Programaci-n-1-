#Inicio de sesion
Usuario = "Angiesuarez"
Contraseña = 123456
#Solicitar nombre de usuario y contraseña
input_Usuario = input("Ingrese su nombre de usuario")
input_Contraseña = int(input("Ingrese su contraseña"))
if input_Usuario == Usuario and input_Contraseña == Contraseña:
    print("inicio de sesion exitoso")
else:
    print("Usuario o Contraseña incorrecta")
