#3.Realice un programa para el cálculo de volúmenes (Prisma, Pirámide, Cono truncado, Cilindro)
#donde el usuario pueda seleccionar el sólido y los parámetros de cada volumen. 
import math

# Funciones para calcular el volumen de cada sólido
def volumen_prisma(base, altura):
    return base * altura

def volumen_piramide(base, altura):
    return (1/3) * base * altura

def volumen_cono_truncado(radio1, radio2, altura):
    return (1/3) * math.pi * altura * (radio1**2 + radio1*radio2 + radio2**2)

def volumen_cilindro(radio, altura):
    return math.pi * radio**2 * altura

# Diccionario que mapea las opciones del usuario a las funciones de cálculo de volumen
opciones = {
    1: volumen_prisma,
    2: volumen_piramide,
    3: volumen_cono_truncado,
    4: volumen_cilindro
}

# Función principal
def main():
    opcion = int(input("Seleccione el sólido para calcular su volumen:\n1. Prisma\n2. Pirámide\n3. Cono Truncado\n4. Cilindro\n"))

    if opcion not in opciones:
        print("Opción no válida.")
        return

    parametros = []

    # Solicitar los parámetros necesarios para el cálculo del volumen
    for parametro in opciones[opcion].__code__.co_varnames:
        if parametro != 'altura':
            valor = float(input(f"Ingrese la medida de {parametro}: "))
            parametros.append(valor)
        else:
            altura = float(input("Ingrese la altura: "))
            parametros.append(altura)

    # Calcular el volumen y mostrar el resultado
    volumen = opciones[opcion](*parametros)
    print("El volumen del sólido seleccionado es:", volumen)

if __name__ == "__main__":
    main()