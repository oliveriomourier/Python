#Ejercicio 6.5. Escribir una función que dada una cadena de caracteres, devuelva:
#a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
#devolver 'USB' .

def devolverIniciales(palabra):
    palabraSeparada = palabra.split()
    iniciales = ""
    
    for palabra in palabraSeparada:
        iniciales += palabra[0]
        
    return iniciales

#print(devolverIniciales('Universal Serial Bus'))
    

#b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
#'república argentina' debe devolver 'República Argentina' .

def devolverInicialess(palabra):
    palabraSeparada = palabra.split()
    
    for palabra in palabraSeparada:
        print(palabra.capitalize(), end=" ")

devolverInicialess('republica argentina')



#c) Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer'
#debe devolver 'Antes ayer'