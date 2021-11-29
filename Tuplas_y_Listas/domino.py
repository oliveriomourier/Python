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

