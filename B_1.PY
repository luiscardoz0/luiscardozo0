#1.Realice un programa que calcule la potencia que consume un circuito ingresando por teclado el
#valor de corriente y voltaje.
# Solicitar al usuario que ingrese el voltaje y la corriente
voltaje = float(input("Ingrese el valor del voltaje (en voltios): "))
corriente = float(input("Ingrese el valor de la corriente (en amperios): "))

# Calcular la potencia y mostrar el resultado
print("La potencia consumida por el circuito es:", voltaje * corriente, "vatios.")