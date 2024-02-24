#4.Realice un programa que le permita al usuario escoger entre robot Cilíndrico, Cartesiano y esférico,
#donde como respuesta a la selección conteste con el tipo y número de articulaciones que posee.
def main():
    print("Seleccione el tipo de robot:")
    print("1. Robot Cilíndrico")
    print("2. Robot Cartesiano")
    print("3. Robot Esférico")

    opcion = int(input("Ingrese el número de opción: "))

    if opcion == 1:
        print("\nRobot Cilíndrico")
        print("Número de articulaciones: 3")
    elif opcion == 2:
        print("\nRobot Cartesiano")
        print("Número de articulaciones: 3")
    elif opcion == 3:
        print("\nRobot Esférico")
        print("Número de articulaciones: 3")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()