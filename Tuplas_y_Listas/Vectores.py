#Vectores
#a) Escribir una función que reciba dos vectores y devuelva su producto escalar.

def productoEscalar(vector1, vector2):
    escalar = 0
    
    for i in range(len(vector1)):
        escalar += vector1[i] * vector2[i]
        
    return escalar

#print(productoEscalar((1,5,-2), (3,1, 2)))

#b) Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.

def sonOrtogonales(vector1, vector2):
    escalar = productoEscalar(vector1, vector2)
    if escalar:
        print("Somos dos vectores ortogonales")
    else:
        print("No somos vectores ortogonales")
        
sonOrtogonales((1,5,-2), (2, 0,1))
#c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.
#d) Escribir una función que reciba un vector y devuelva su norma.