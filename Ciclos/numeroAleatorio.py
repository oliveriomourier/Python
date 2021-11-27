#Utilizando la función randrange del módulo random , escribir un programa que
#obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
#si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número
#correcto.
import random 

def acertarNumero(numero):
    numAletorio = random.randrange(numero)
    numUsuario = int(input("Ingrese un numero: "))
    
    while(numAletorio != numUsuario):
        print("Error! "+str(numUsuario)+" no es el numero aleatorio, vuelva a intentarlo")
        numUsuario = int(input("Ingrese un numero: "))
        
    print("Correcto "+ str(numUsuario) + " es el numero aleatorio")
    
acertarNumero(10)