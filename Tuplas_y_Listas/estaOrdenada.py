#Escribir una función que reciba una tupla de elementos e indique si se encuentran
#ordenados de menor a mayor o no.

def estaOrdenado(tupla):
    if len(tupla) == 1:
        print ("La tupla no esta ordenada")
        return True
        
    for i in range(1, len(tupla)):
        if(tupla[i]<tupla[i-1]):
            print ("La tupla no esta ordenada")
            return True
        
    print ("La tupla esta ordenada")
    return False
    
estaOrdenado(())
            
            