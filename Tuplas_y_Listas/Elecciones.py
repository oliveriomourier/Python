#Campaña electoral
#a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima
#el mensaje Estimado <nombre>, vote por mí.

def imprimirPedidoDeVoto(tupla):
    
    for nombre in tupla:
        print(f"Estimado {nombre}, vote por mi")

#b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una
#cantidad n , e imprima el mensaje anterior para los n nombres que se encuentran a partir
#de la posición p .
#c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario,
#para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género.
        
    
imprimirPedidoDeVoto(("Oliverio", "Juan", "Manuel"))