#Ejercicio 9.2. Diccionarios usados para contar.
#a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
#de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
#hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1} .

def contarAparicionesPalabras(cadena):
    diccionario = {}
    listaPalabras = cadena.lower().split()
    
    for palabra in listaPalabras:
        if palabra in diccionario:
            diccionario[palabra] += 1;
        else:
            diccionario[palabra] = 1;
            
    return diccionario

#print(contarAparicionesPalabras("Que lindo día que hace hoy"))

#b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una ca-
#dena de texto, y los devuelva en un diccionario.

def contarAparicionesCaracteres(cadena):
    diccionario = {}
    cadenaLower = cadena.lower()
    
    for caracter in cadenaLower:
        if caracter in diccionario:
            diccionario[caracter] += 1;
        else:
            diccionario[caracter] = 1;
            
    return diccionario


#print(contarAparicionesCaracteres("Que lindo día que hace hoy"))


    









