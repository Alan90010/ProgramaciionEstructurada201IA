UMBRAL_PEQUENO = 5.0
UMBRAL_GRANDE = 20.0

def calcular_volumen(dimension):
    return dimension ** 3

def clasificar_objeto(dimension):
    if dimension <= 0:
        return "Error: Lectura inválida."
    elif dimension <= UMBRAL_PEQUENO:
        return "Clasificación: Micro-componente (Grado A)"
    elif dimension <= UMBRAL_GRANDE:
        return "Clasificación: Componente Estándar (Grado B)"
    else:
        return "Clasificación: Componente Industrial (Grado C)"

def main():
    try:
        valor = float(input("Ingrese el tamaño (cm): "))
        
        resultado = clasificar_objeto(valor)
        print(resultado)
        
        if "Industrial" in resultado:
            vol = calcular_volumen(valor)
            print(f"Espacio requerido: {vol} cm3")
            
        print("Registro de inspección completado.")
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()