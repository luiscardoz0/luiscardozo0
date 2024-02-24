#4.Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de
#la temperatura.
def calcular_resistencia(temp):
    # Coeficientes de la ecuación de Callendar-Van Dusen
    a = 3.9083e-3
    b = -5.775e-7
    # Temperatura de referencia
    t0 = 100.0
    # Resistencia a temperatura de referencia
    r0 = 100.0

    # Cálculo de la resistencia
    r = r0 * (1 + a * temp + b * temp**2)

    return r

# Temperatura en grados Celsius
temperatura = 25.0

# Calcular resistencia
resistencia = calcular_resistencia(temperatura)

# Imprimir resultado
print(f"La resistencia de la RTD a {temperatura} grados Celsius es {resistencia} ohmios.")