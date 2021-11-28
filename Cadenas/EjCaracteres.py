#Escribir funciones que dada una cadena de caracteres:


#a) Imprima los dos primeros caracteres.
def imprimirPrimerosDosCaracteres(palabra):
    if len(palabra)>= 2:
        print(palabra[:2])
    else:
        print("La palabra debe tener mas de un caracter!")
        
        
imprimirPrimerosDosCaracteres("Oliver!")
imprimirPrimerosDosCaracteres("q")


#b) Imprima los tres últimos caracteres.
def imprimirUltimosTresCaracteres(palabra):
    if len(palabra)>3:
        print(palabra[-3:])
    else:
        print("Ingrese una palabra mas larga!")
    
    
imprimirUltimosTresCaracteres("Perro")
imprimirPrimerosDosCaracteres("q")

#c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'

def imprimirCadaDosCaracteres(palabra):
    print(palabra[::2])
    
    
imprimirCadaDosCaracteres("recta")


#Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
def imprimirInverso(palabra):
    print(palabra[::-1])
    

imprimirInverso("hola mundo!")


#Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
#'reflejoojelfer' .
def imprimirReflejo(palabra):
    print(palabra + palabra[::-1])
    

imprimirReflejo("reflejo")

