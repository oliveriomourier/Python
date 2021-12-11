#Ejercicio 9.1. Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario
#en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los
#segundos.
#Por ejemplo:
#13>>> l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'),
#('Buenos', 'días') ]
#>>> print(tuplas_a_diccionario(l))
#{ 'Hola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }

def convertirTuplaADiccionario(listaDeTuplas):
    diccionario = {}
    
    for elemento in listaDeTuplas:
        if elemento[0] in diccionario:
            diccionario[elemento[0]].append(elemento[1])
        else:
            diccionario[elemento[0]] = [elemento[1]]
            
    return diccionario

print(convertirTuplaADiccionario([ ('Hola', 'don Pepito'), ('Hola', 'don Jose'),('Buenos', 'días') ]))