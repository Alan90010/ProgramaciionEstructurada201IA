def contraseña():
    intentos = 0
    clave_correcta = '1234'

    while intentos < 3:
        contraseña = input("Ingrese contraseña: ")

        if contraseña == clave_correcta:
            print("Acceso Concedido")
            return 
        
        else:
            intentos = intentos + 1
            print("Contraseña incorrecta")
    print("Cuenta bloqueada")

def main():
    contraseña()

if __name__ == "__main__":
    main()