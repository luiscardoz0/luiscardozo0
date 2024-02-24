#3.Realice un programa que convierta coordenadas rectangulares a cilíndricas y esféricas, para lo cual
#deben consultar sobre el uso de funciones trigonométricas en Python. 
import math

def rectangular_a_cilindricas(x, y, z):
    rho = math.sqrt(x**2 + y**2)
    phi = math.atan2(y, x)
    return rho, phi, z

def rectangular_a_esfericas(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    theta = math.acos(z / r)
    phi = math.atan2(y, x)
    return r, theta, phi

# Ejemplo de uso
x, y, z = 3, 4, 5

# Convertir a cilíndricas
rho, phi, z_cil = rectangular_a_cilindricas(x, y, z)
print(f"Coordenadas Cilíndricas: ρ = {rho}, φ = {math.degrees(phi)}, z = {z_cil}")

# Convertir a esféricas
r, theta, phi = rectangular_a_esfericas(x, y, z)
print(f"Coordenadas Esféricas: r = {r}, θ = {math.degrees(theta)}, φ = {math.degrees(phi)}")
