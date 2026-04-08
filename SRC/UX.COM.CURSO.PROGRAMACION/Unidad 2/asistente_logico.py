import datetime

def clasificar_intencion(frase, nombre_asistente):

    frase = frase.lower()

    if "hola" in frase or "buenos días" in frase:
        print(f"¡Hola! Soy {nombre_asistente}. Es un gusto saludarte.")

    elif "clima" in frase or "temperatura" in frase:
        print("Consultando el servicio meteorológico... Hoy en Xalapa tendremos un día nublado.")

    elif "hora" in frase or "tiempo" in frase:
        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"La hora actual del sistema es: {hora_actual}")

    else:
        print("Lo siento, todavía no entiendo ese comando. ¿Podrías intentar con otra palabra?")

def main():
 
    nombre_asistente = "IA-UX"
    print(f"--- Bienvenido al sistema {nombre_asistente} ---")

    entrada_usuario = input("¿En qué puedo ayudarte hoy?: ")

    clasificar_intencion(entrada_usuario, nombre_asistente)

    print(f"Proceso finalizado. Gracias por usar {nombre_asistente}.")

if __name__ == "__main__":
    main()