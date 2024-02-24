#1.Realice un programa que grafique el comportamiento de un sensor PT100 desde -200°C a 200°C

import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la resistencia de la PT100
def resistencia_pt100(temperatura):
    # Coeficientes de la ecuación de Callendar-Van Dusen
    a = 3.9083e-3
    b = -5.775e-7
    R0 = 100.0  # Resistencia a 0°C

    return R0 * (1 + a * temperatura + b * temperatura**2)

# Rango de temperaturas de -200°C a 200°C
temperaturas = np.linspace(-200, 200, 1000)

# Calcular las resistencias correspondientes
resistencias = resistencia_pt100(temperaturas)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(temperaturas, resistencias, color='blue')
plt.title('Comportamiento de un sensor PT100')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ohm)')
plt.grid(True)
plt.show()