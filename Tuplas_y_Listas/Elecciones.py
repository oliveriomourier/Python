#Campaña electoral
#a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima
#el mensaje Estimado <nombre>, vote por mí.

def imprimirPedidoDeVoto(tupla):
    
    for nombre in tupla:
        print(f"Estimado {nombre}, vote por mi")


#imprimirPedidoDeVoto(("Oliverio", "Juan", "Manuel"))
#b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una
#cantidad n , e imprima el mensaje anterior para los n nombres que se encuentran a partir
#de la posición p .
        
def imprimirDesdeHasta(tuplaNombres, origen, final):
    
    for i in range(origen, origen + final):
        print(f"Estimado {tuplaNombres[i]}, vote por mi")
    
#imprimirDesdeHasta(("Oliverio", "juan", "manuel", "seba", "pino", "alberto", "elOgro"), 2, 1)  
    
    
#c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario,
#para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género.


def imprimirPorGenero(tupla_de_tuplas, origen, final):
    nombre = 0
    genero = 1
    for i in range(origen, origen + final):
        if tupla_de_tuplas[i][genero] == "Masculino":
            print(f"Estimado {tupla_de_tuplas[i][nombre]}, vote por mi")
        else:
            print(f"Estimada {tupla_de_tuplas[i][nombre]}, vote por mi")
        
        
        
        
imprimirPorGenero((("Oliverio", "Masculino"), ("juan", "Masculino"), ("manuela", "Femenino"), ("Emilia", "Femenino"), ("Raquel", "Femenino"), ("alberto", "Masculino"), ("Anabela", "Femenino")), 1, 3)  
        
        
        
        
        
        
        
        
        
        
        
        
        
    