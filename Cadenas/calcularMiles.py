#Ejercicio 6.4. Escribir una función que reciba una cadena que contiene un largo número en-
#tero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe
#'1234567890' , debe devolver '1.234.567.890' .

def calculcarMiles(numero):
    numeroNuevo = ""
    for i in range(len(numero)-1, -1, -1):
        if i%3 == 0 and i != len(numero)-1:
            numeroNuevo += "."
        numeroNuevo += numero[i]
    print(numeroNuevo[::-1])
        
calculcarMiles('1234567890' )