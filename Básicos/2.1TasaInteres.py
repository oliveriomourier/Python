#Ejercicio 2.1. Escribir una función que reciba una cantidad de pesos, una tasa de interés y un
#número de años y devuelva el monto final a obtener. La fórmula a utilizar es:
#𝐶 𝑛 = 𝐶 × (1 +
#𝑥 𝑛
#)
#100
#Donde 𝐶 es el capital inicial, 𝑥 es la tasa de interés y 𝑛 es el número de años a calcular.

def montoFinal(pesos, interes, anios):
    return pesos * (1 + interes/100)**anios

print(round(montoFinal(100, 5, 5), 2))

#Ejercicio 2.2. Utilizando la función del ejercicio anterior, escribir un programa que le pregunte
#al usuario la cantidad de pesos inicial, la tasa de interés y el número de años y muestre el monto
#final a obtener.

def ingresarPesosInteresAnios():
    pesos = int(input("Ingrese la cantidad de pesos iniciales: "))
    interes = int(input("Ingrese la tasa de interes: "))
    anios = int(input("Ingrese la cantidad de anios: "))
    
    return pesos, interes, anios

def main():
    pesos, interes, anios = ingresarPesosInteresAnios()
    print(round(montoFinal(pesos, interes, anios), 2))
    
main()