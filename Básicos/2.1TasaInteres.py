#Ejercicio 2.1. Escribir una función que reciba una cantidad de pesos, una tasa de interés y un
#número de años y devuelva el monto final a obtener. La fórmula a utilizar es:
#𝐶 𝑛 = 𝐶 × (1 +
#𝑥 𝑛
#)
#100
#Donde 𝐶 es el capital inicial, 𝑥 es la tasa de interés y 𝑛 es el número de años a calcular.

def montoFinal(pesos, interes, anios):
    return pesos * (1 + interes/100)**anios

print(montoFinal(100, 5, 5))