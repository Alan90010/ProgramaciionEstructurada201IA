# Impletmentacion de Match em Python

def demostracion():
    opcion = input("Ingrese una opcion (1-7):")

    match opcion:
        case "1":
            print("Opcion 1 seleccionada")
            print(f"Lunes")
        case "2":
            print("Opcion 2 seleccionada")
            print(f"Martes")
        case "3":
            print("Opcion 3 seleccionada")
            print(f"Miercoles")
        case "4":
            print("Opcion 4 seleccionada")
            print(f"Jueves") 
        case "5":
            print("Opcion 5 seleccionada")
            print(f"Viernes")  
        case "6":
            print("Opcion 6 seleccionada")
            print(f"Sabado")
        case "7":
            print("Opcion 7 seleccionada")
            print(f"Domingo")
        case _:
            print("Opcion no valida0")

def main():
    demostracion()

if __name__ == "__main__":
    main()