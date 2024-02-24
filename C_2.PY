#.2 Realice un programa que le permita al usuario ingresar los coeficientes de una función de
#transferencia de segundo orden y graficar su comportamiento, además se debe mostrar que tipo
#de sistema es: subamortiguado, criticamente amortiguado y sobreamortiguado.
import numpy as np
import matplotlib.pyplot as plt

# Coeficientes de la función de transferencia
K = float(input("Ingrese la ganancia del sistema (K): "))
zeta = float(input("Ingrese el factor de amortiguamiento (zeta): "))
omega_n = float(input("Ingrese la frecuencia natural no amortiguada (omega_n): "))

# Graficar la respuesta en frecuencia
s = np.linspace(0, 10, 1000)
H = K / (s**2 + 2 * zeta * omega_n * s + omega_n**2)
plt.plot(s, np.abs(H))
plt.title('Respuesta en Frecuencia')
plt.xlabel('Frecuencia Angular (s)')
plt.ylabel('|H(s)|')
plt.grid(True)
plt.show()

# Determinar y mostrar el tipo de sistema
if zeta < 1:
    print("El sistema es subamortiguado.")
elif zeta == 1:
    print("El sistema es críticamente amortiguado.")
else:
    print("El sistema es sobreamortiguado.")