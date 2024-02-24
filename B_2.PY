#2.Realice un programa que calcule X números aleatorios en un rango determinado por el usuario.
import random

def generar_numeros_aleatorios(cantidad, rango_min, rango_max):
    numeros_aleatorios = []
    for _ in range(cantidad):
        numero_aleatorio = random.uniform(rango_min, rango_max)
        numeros_aleatorios.append(numero_aleatorio)
    return numeros_aleatorios

# Entradas del usuario
cantidad_numeros = int(input("Ingrese la cantidad de números aleatorios a generar: "))
rango_min = float(input("Ingrese el límite inferior del rango: "))
rango_max = float(input("Ingrese el límite superior del rango: "))

# Generar números aleatorios
numeros_generados = generar_numeros_aleatorios(cantidad_numeros, rango_min, rango_max)

# Mostrar resultados
print(f"{cantidad_numeros} números aleatorios en el rango [{rango_min}, {rango_max}]:")
print(numeros_generados)