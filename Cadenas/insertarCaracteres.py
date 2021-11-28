#Escribir funciones que dada una cadena y un caracter:
#a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
#'s,e,p,a,r,a,r'

def insertarCaracter(palabra):
    palabraConCaracter=""
    
    for i in range(len(palabra)):
        palabraConCaracter += palabra[i]+","
        
    return palabraConCaracter[:len(palabraConCaracter)-1]

print(insertarCaracter("perro"))


#b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
#debería devolver 'mi_archivo_de_texto.txt'

def reemplazarEspacioPorCaracter(palabra, caracter):
    palabraSeparada = palabra.split()
    return caracter.join(palabraSeparada)

print(reemplazarEspacioPorCaracter('mi archivo de texto.txt', '_'))


#c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y
#'X' debería devolver 'su clave es: XXXX'

def reemplazarDigitos(palabra):
    palabraSinDigitos = ""
    
    for i in range(len(palabra)):
        if(palabra[i].isnumeric()):
            palabraSinDigitos += "X"
        else:
            palabraSinDigitos += palabra[i]
    
    return palabraSinDigitos

print(reemplazarDigitos('su clave es: 1540'))
    
    
#d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver
#'255.255.255.0'

def insertarCaracterCadaTres(palabra, caracter):
    palabraNueva = ""
    
    for i in range(len(palabra)):
        if i%3 == 0 and i!=0:
            palabraNueva += caracter
        palabraNueva += palabra[i]
            
    return palabraNueva

print(insertarCaracterCadaTres('2552552550', '.'))
    

