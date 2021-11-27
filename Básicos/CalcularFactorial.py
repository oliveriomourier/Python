#Dado un numero entero calcular su factorial

def factorialRecursivo(numero):
    if numero == 1:
        return 1
    
    return numero * factorialRecursivo(numero -1)

numero =factorialRecursivo(5)
print(str(numero))

def calcularFactorial(numero):
    if not numero > 0 :
        print("El numero debe ser entero mayor a 0")
        return
    
    for i in range(1, numero):
        numero *= i
        
    return numero
        
numero2 = calcularFactorial(5)
print(str(numero2))


