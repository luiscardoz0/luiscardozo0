import numpy as np
import matplotlib.pyplot as plt

# Solicitar al usuario los valores de V (voltaje), R (resistencia) y C (capacitancia)
V0 = float(input("Ingrese el valor del voltaje (V): "))
R = float(input("Ingrese el valor de la resistencia (Ω): "))
C = float(input("Ingrese el valor de la capacitancia (μF): ")) * 1e-6  # Convertir μF a F

# Calcular la constante de tiempo
tau = R * C

# Definir el rango de tiempo para la simulación
t = np.linspace(0, 5*tau, 1000)  # 5 constantes de tiempo para visualizar la carga/descarga completa

# Ecuaciones de carga y descarga
V_carga = V0 * (1 - np.exp(-t / tau))
V_descarga = V0 * np.exp(-t / tau)

# Gráfica
plt.figure(figsize=(10, 6))
plt.plot(t, V_carga, label='Carga del Capacitor')
plt.plot(t, V_descarga, '--', label='Descarga del Capacitor')

# Etiquetas y leyenda
plt.title('Carga y Descarga de un Circuito RC')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.legend()
plt.grid(True)

# Mostrar gráfica
plt.show()