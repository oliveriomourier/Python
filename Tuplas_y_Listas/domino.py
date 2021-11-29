#Dominó.
#a) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
#recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)

def lasFichasEncajan(tupla1, tupla2):
    encajan = False
    
    for elemento in tupla1:
        if elemento in tupla2:
            encajan = True
            return encajan
        
    return encajan

print(lasFichasEncajan((1,4), (1,2)))
print(lasFichasEncajan((1,1), (4,4)))


#b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
#recibidas en una cadena, por ejemplo: 3-4 2-5 . Nota: utilizar la función split de las
#cadenas.

def fichasEncajan(cadena1, cadena2):
    cadena1Separada = cadena1.split('-')
    cadena2Separada = cadena2.split('-')
    encajan = False
    
    for elemento in cadena1Separada:
        if elemento in cadena2Separada:
            encajan = True
            return encajan
    
    return encajan

print(fichasEncajan("1-4", "1-2"))
print(fichasEncajan("1-1", "4-4"))