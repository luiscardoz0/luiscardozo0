#5.Escribir un programa que realice la pregunta ¿Desea continuar Si/No? y que no deje de hacerla
#hasta que el usuario teclee No.
def continuar():
    while True:
        respuesta = input("¿Desea continuar? (Si/No): ").strip().lower()
        if respuesta == 'no':
            print("ok")
            break
        elif respuesta != 'si':
            print("si o no")

continuar()