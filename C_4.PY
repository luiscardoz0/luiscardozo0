import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def dibujar_sistema_coordenado():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Ejes X, Y, Z
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.1)

    # Etiquetas de los ejes
    ax.text(1.1, 0, 0, 'X')
    ax.text(0, 1.1, 0, 'Y')
    ax.text(0, 0, 1.1, 'Z')

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

def dibujar_vector(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Vector
    ax.quiver(0, 0, 0, x, y, z, color='m', arrow_length_ratio=0.1)

    # Origen
    ax.scatter(0, 0, 0, color='k', s=50)

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# Solicitar coordenadas al usuario
x = float(input("Ingrese la coordenada X del vector: "))
y = float(input("Ingrese la coordenada Y del vector: "))
z = float(input("Ingrese la coordenada Z del vector: "))

# Dibujar sistema de coordenadas
dibujar_sistema_coordenado()

# Dibujar vector ingresado por el usuario
dibujar_vector(x, y, z)