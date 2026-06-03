"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte II)
Alumno: [Alan]
"""
import random  # Única librería importada por el novato
import math # Tiene funciones matematicas y nos ayuda a simplificar el codigo 

# =====================================================================
# RETO 1: Formateador de Nombres de Usuario para Discord
# Sentido: Asegurar que los nombres en la base de datos no tengan espacios
#          extras y que inicien con mayúscula (Formato Limpio).
# Problema: Limpieza manual carácter por carácter usando bucles.
# =====================================================================
def limpiar_nombre_usuario(nombre_sucio):
    # Cambie los bucles while que recorrian caracter por caracter los nombres para buscar el inicio y el fin, "strip" hace lo mismo pero en un solo comando
    nombre_sin_espacios = nombre_sucio.strip()
    
    # Se cambio la parte de la primera letra mayuscula ya que el comando ".capitalize" hace que la primera letra se mayuscula y las demas minusculas
    if len(nombre_sin_espacios) > 0:
        return nombre_sin_espacios.capitalize()
    return ""

# =====================================================================
# RETO 2: Buscador de Palabras Prohibidas (Filtro contra Groserías)
# Sentido: Banear o censurar mensajes inapropiados en el chat del servidor.
# Problema: Uso innecesario de un ciclo indexado para buscar subcadenas.
# =====================================================================
def contiene_palabra_bloqueada(mensaje_chat, palabra_prohibida):
    largo_mensaje = len(mensaje_chat)
    largo_palabra = len(palabra_prohibida)
    
    # Recorre el mensaje buscando coincidencia exacta letra por letra
    for i in range(largo_mensaje - largo_palabra + 1):
        coincidencia = True
        for j in range(largo_palabra):
            if mensaje_chat[i + j] != palabra_prohibida[j]:
                coincidencia = False
                break
        if coincidencia:
            return True
            
    return False

def contiene_palabra_bloqueada(mensaje_chat, palabra_prohibida):
    largo_mensaje = len(mensaje_chat)
    largo_palabra = len(palabra_prohibida)
 
    # Se cambio que se deje de hacer la comparacion letra a letra para hacer una comparacion en un tipo de cadena 
    for i in range(largo_mensaje - largo_palabra + 1):
        if mensaje_chat[i:i + largo_palabra] == palabra_prohibida:
            return True
 
    return False
 

# =====================================================================
# RETO 3: Generador de Contraseñas Temporales para Nuevos Usuarios
# Sentido: Asignar una clave alfanumérica segura al registrar un agente.
# Problema: Algoritmo ineficiente para concatenar elementos aleatorios.
# =====================================================================

def generar_clave_temporal():
    caracteres_validos = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
    clave_generada = ""
 
 # Solo elimine la variable "indice_aleatorio" para que se generara en una sola linea
    for i in range(8):
        clave_generada += caracteres_validos[random.randint(0, len(caracteres_validos) - 1)]
 
    return clave_generada

# =====================================================================
# RETO 4: Buscador del Valor Central (Mediana de Latencia de Red)
# Sentido: Encontrar el punto medio de ping (ms) para evaluar lag.
# Problema: Implementación manual de un ordenamiento complejo (Burbuja) 
#           y cálculo manual de la mediana.
# =====================================================================
def calcular_mediana_latencia(lista_pings):
    # Clonamos la lista para no alterar la original
    pings_ordenados = list(lista_pings)
    n = len(pings_ordenados)
    
    # Método de la burbuja manual para ordenar los pings de menor a mayor
    for i in range(n):
        for j in range(0, n - i - 1):
            if pings_ordenados[j] > pings_ordenados[j + 1]:
                # Intercambio manual de variables
                temporal = pings_ordenados[j]
                pings_ordenados[j] = pings_ordenados[j + 1]
                pings_ordenados[j + 1] = temporal
                
    # Cálculo manual del elemento central (Mediana)
    if n % 2 == 1:
        return pings_ordenados[n // 2]
    else:
        mitad1 = pings_ordenados[(n // 2) - 1]
        mitad2 = pings_ordenados[n // 2]
        return (mitad1 + mitad2) / 2.0

def calcular_mediana_latencia(lista_pings):
    pings_ordenados = list(lista_pings)
    n = len(pings_ordenados)

    for i in range(n):
        for j in range(0, n - i - 1):
            if pings_ordenados[j] > pings_ordenados[j + 1]:
                temporal = pings_ordenados[j]
                pings_ordenados[j] = pings_ordenados[j + 1]
                pings_ordenados[j + 1] = temporal
 
 # Solo agregue el math para dejar mas visual las operaciones que se realizan 
    if n % 2 == 1:
        return pings_ordenados[math.floor(n / 2)]
    else:
        mitad1 = pings_ordenados[math.floor(n / 2) - 1]
        mitad2 = pings_ordenados[math.floor(n / 2)]
        return (mitad1 + mitad2) / 2.0

# === PROGRAMA PRINCIPAL (Punto de entrada para probar) ===
if __name__ == "__main__":
    print("--- Probando Código Inicial (Parte II) ---")
    
    print("Usuario limpio:", [limpiar_nombre_usuario("   luNA_eDUaRDo  ")])
    
    msg = "No digas malas palabras en este servidor"
    print("¿Tiene groserías?:", contiene_palabra_bloqueada(msg, "malas"))
    
    print("Clave generada por el sistema:", generar_clave_temporal())
    
    pings_servidor = [120, 45, 80, 23, 150, 62]
    print("Mediana de latencia encontrada:", calcular_mediana_latencia(pings_servidor))