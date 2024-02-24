#2.Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
#matrices previamente inicializadas.
import numpy as np

matrizA = np.array([[1,2],[3,4],[5,6]],float)
matrizB = np.array([[4,6],[4,3],[1,2]],float)
suma=matrizA + matrizB
resta=matrizA-matrizB
multiplicacion=matrizA*matrizB
divicion=matrizA*matrizB
print(f"suma de matrices: \n {suma} \n resta de matrices: \n {resta} \n multiplicacion de matrices: \n {multiplicacion} \n divicion de matrices:\n {divicion}")