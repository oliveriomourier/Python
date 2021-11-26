#Pedir dos número al usuario y devolver el producto

def solicitarNumerosYMultiplicar():
    
    primerNumero = int(input("Ingrese el primer número:"))
    segundoNumero = int(input("Ingrese el segundo número:"))
    producto = primerNumero * segundoNumero
    
    print("El resultado es "+ str(producto))
    return producto

solicitarNumerosYMultiplicar()