#5.Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo)
#y un parámetro de salida (matriz).
import numpy as np

# Función para la rotación en el eje X
def rotacion_x(angulo):
    radianes = np.radians(angulo)
    matriz_rotacion_x = np.array([
        [1, 0, 0],
        [0, np.cos(radianes), -np.sin(radianes)],
        [0, np.sin(radianes), np.cos(radianes)]
    ])
    return matriz_rotacion_x

# Función para la rotación en el eje Y
def rotacion_y(angulo):
    radianes = np.radians(angulo)
    matriz_rotacion_y = np.array([
        [np.cos(radianes), 0, np.sin(radianes)],
        [0, 1, 0],
        [-np.sin(radianes), 0, np.cos(radianes)]
    ])
    return matriz_rotacion_y

# Función para la rotación en el eje Z
def rotacion_z(angulo):
    radianes = np.radians(angulo)
    matriz_rotacion_z = np.array([
        [np.cos(radianes), -np.sin(radianes), 0],
        [np.sin(radianes), np.cos(radianes), 0],
        [0, 0, 1]
    ])
    return matriz_rotacion_z

# Ejemplo de uso
angulo = 60  # Ángulo en grados


# Rotación en el eje X
print("Angulo de rotación", angulo)
matriz_rotacion_x = rotacion_x(angulo)
print("Matriz de rotación en el eje X:")
print(matriz_rotacion_x)

# Rotación en el eje Y
print("Angulo de rotación", angulo)
matriz_rotacion_y = rotacion_y(angulo)
print("\nMatriz de rotación en el eje Y:")
print(matriz_rotacion_y)

# Rotación en el eje Z
print("Angulo de rotación", angulo)
matriz_rotacion_z = rotacion_z(angulo)
print("\nMatriz de rotación en el eje Z:")
print(matriz_rotacion_z)