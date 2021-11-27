#Escribir un programa que contenga una contraseña inventada, que le pregunte al usua-
#rio la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.

def contraseniaCorrecta():
    
    contrasenia = "soyLaPassCorrecta"
    intentoUsuario = input("Ingrese la contraseña: ")
    
    while contrasenia != intentoUsuario:
        print("contraseña inválida!")
        intentoUsuario = input("Ingrese la contraseña: ")
        
    print("contraseña válida!")
    
#contraseniaCorrecta()

#Modificar el programa anterior para que solamente permita una cantidad fija de inten-
#tos.

def passConIntentos():
    
    cantMaxIntentos = 5
    i = 1
    contrasenia = "soyLaPassCorrecta"
    intentoUsuario = input("Ingrese la contraseña: ")
    
    while i<cantMaxIntentos and contrasenia != intentoUsuario:
        print("Contraseña inválida!")
        i += 1
        intentoUsuario = input("Ingrese la contraseña: ")
        
    if contrasenia == intentoUsuario:
        print("Contraseña valida!")
    else:
        print("Cantidad máxima de intentos!")
        
passConIntentos()
        