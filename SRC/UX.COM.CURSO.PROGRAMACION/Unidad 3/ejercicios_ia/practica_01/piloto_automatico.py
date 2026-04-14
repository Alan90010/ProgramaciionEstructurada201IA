def procesar_navegacion():
    distancia = float(input("¿A qué distancia está el objeto más cercano (en metros)?: "))
    semaforo = input("¿De qué color está el semáforo? (verde/amarillo/rojo): ").lower()
    peaton = input("¿Hay un peatón cruzando? (si/no): ").lower()

    if distancia < 5 or peaton == "si":
        print("¡FRENO DE EMERGENCIA ACTIVADO! Deteniendo el vehículo inmediatamente.")
    
    elif semaforo == "rojo":
        print("Estado: Detenido. Esperando luz verde.")
        
    elif semaforo == "amarillo":
        print("Estado: Precaución. Reduciendo velocidad para detenerse.")
        
    elif semaforo == "verde":
        print("Estado: En movimiento. Todo despejado para avanzar.")
    
    if semaforo not in ["verde", "amarillo", "rojo"]:
        print("Error de lectura en sensores: Color de semáforo no reconocido.")

    print("Monitoreo de sensores constante... Sistema activo.")

def main():
    procesar_navegacion()

if __name__ == "__main__":
    main()