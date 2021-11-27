#Escribir un programa que permita al usuario ingresar un conjunto de notas, pre-
#guntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.

def promedioNotas():
    
    cantNotas = 0
    sumatoriaNotas = 0
    seguir = True
    
    while seguir:
        nota = int(input("Ingrese una nota: "))
        cantNotas+= 1
        sumatoriaNotas += nota
        
        continuar = input("Desea ingresar otra nota? [S/n]: ")
        if continuar == "n":
            seguir = False
          
    return sumatoriaNotas / cantNotas

promedio = promedioNotas()
print(promedio)


