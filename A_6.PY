#6.Realice un programa que calcule la fuerza de avance y retroceso de un cilindro neumático de doble
#efecto. Debe establecer previamente los valores de presión, así como las dimensiones físicas del
#cilindro para realizar el cálculo.
import math

def calcular_fuerza_avance(presion, radio_piston):
    area_avance = math.pi * (radio_piston ** 2)
    return presion * area_avance

def calcular_fuerza_retroceso(presion, radio_piston, diametro_varilla):
    radio_varilla = diametro_varilla / 2
    area_retroceso = math.pi * (radio_piston * 2) - math.pi * (radio_varilla * 2)
    return presion * area_retroceso

# Parametros del cilindro
presion = 8 #bares
print("La presión en bares es: ",presion)
radio_piston = 0.02 
print("El radio en metros es: ",radio_piston)
diametro_varilla = 0.01
print("El diametro del vastago en metros es:  ",radio_piston)

# Cálculo de fuerzas
fuerza_avance = calcular_fuerza_avance(presion, radio_piston)
fuerza_retroceso = calcular_fuerza_retroceso(presion, radio_piston, diametro_varilla)

# Mostrar resultados
print(f"Fuerza de avance: {fuerza_avance} N")
print(f"Fuerza de retroceso: {fuerza_retroceso} N")