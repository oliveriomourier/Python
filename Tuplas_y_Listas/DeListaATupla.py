#Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Ini-
#cial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga primero el
#nombre, luego la inicial con un punto, y luego el apellido.

def listaDeCadenas(ListaDeTuplas):
    listaCadenas = []
    cadena = ""
    
    for tupla in ListaDeTuplas:
        cadena = tupla[1]+" "+tupla[2]+". "+tupla[0]
        listaCadenas.append(cadena)
        
    return listaCadenas

print(listaDeCadenas([("Mou", "Oli", "M"), ("Pelli", "Juan", "C"), ("Came", "Manuel", "S")]))
            