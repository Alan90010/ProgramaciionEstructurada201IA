def datos(lectura):
    LIMITE_SUPERIOR = 100.0
    LIMITE_INFERIOR = 0.0
    
    if lectura >= LIMITE_INFERIOR and lectura <= LIMITE_SUPERIOR:
        datos = lectura / LIMITE_SUPERIOR
        print("Señal aceptada. Valor normalizado para el modelo:", datos)
    else:
        print("Error: Lectura fuera de rango. La señal se considera ruido.")

def main():
    valor = input("Ingrese la lectura del sensor térmico: ")
    lectura = float(valor)
    
    datos(lectura)
    
    print("Fin del proceso de filtrado de datos.")

if __name__ == "__main__":
    main()