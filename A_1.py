#1.Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
#vectores previamente inicializados.
import numpy as np

# Función para realizar la suma de dos vectores
def suma_vectores(v1, v2):
    return v1 + v2

# Función para realizar la resta de dos vectores
def resta_vectores(v1, v2):
    return v1 - v2

# Función para realizar el producto punto entre dos vectores
def producto_punto(v1, v2):
    return np.dot(v1, v2)

# Función para realizar el producto cruz entre dos vectores
def producto_cruz(v1, v2):
    return np.cross(v1, v2)

# Función para realizar la división de dos vectores
def division_vectores(v1, v2):
    # Suponiendo que quieres dividir elemento por elemento
    return v1 / v2

# Vectores de ejemplo
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Suma de vectores
print("Suma:", suma_vectores(vector1, vector2))

# Resta de vectores
print("Resta:", resta_vectores(vector1, vector2))

# Producto punto
print("Producto Punto:", producto_punto(vector1, vector2))

# Producto cruz
print("Producto Cruz:", producto_cruz(vector1, vector2))

# División de vectores
print("División:", division_vectores(vector1, vector2))