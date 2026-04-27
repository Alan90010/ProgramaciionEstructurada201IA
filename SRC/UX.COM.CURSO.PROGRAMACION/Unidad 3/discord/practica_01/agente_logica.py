""" Funcion que recibe un texto y decide que responder. Implementa Programacacion Estrucutura pura. """

def procesar_pregunta(mensasje_usuario):
    #1.Normalizacion (Paso fundamental en IA)
    mensaje = mensasje_usuario.lower().strip()

    #2.Base de conocimiento (Diccionario)
    conocimiento = {
# Concepto de Estructura de Control
"if": "La sentencia 'if' es una estructura condicional que permite ejecutar un bloque de codigo solo si se cumple una condicion (True).",

# Tipos de Datos
"int": "Representa numeros enteros (ej. 5, -10, 0). No incluyen parte decimal.",
 
# Funciones y modularidad
"def": "Es la palabra reservada en Python que se utiliza para definir funciones, permitiendo reutilizar codigo.",

# Operadores y Sintaxis
"print": "Funcion que muestra informacion en la consola o salida estandar.",

# Conceptos de Programacion Estructurada
"algoritmo": "Es un conjunto de pasos ordenados, logicos y finitos que permiten resolver un problema."
    }

    #3.Logica de busqueda
    for clave in conocimiento:
        if clave in mensaje:
            return conocimiento[clave]

    return "Lo siento, aun no se que es eso. !Preguntame sobre variables, funciones o estructuras de control!"


def main():
    print("Hola! Soy tu asistente de programacion. Preguntame sobre variables, funciones o estructuras de control.")
    
    while True:
        user_input = input("Alumno -> ")
        if user_input.lower() == "salir":
            break

        respuesta = procesar_pregunta(user_input)
        print(f"Bot -> {respuesta}")


# Prueba local (Offline)
if __name__ == "__main__":
    main()