# ==========================================
# IMPORTACIÓN DE BIBLIOTECAS
# ==========================================
import sys


# ==========================================
# FUNCIONES GENERADAS POR IA
# ==========================================

def limpiar_lecturas(lista_datos):
    """
    Recibe una lista de lecturas LIDAR y devuelve una nueva lista
    solo con los valores válidos entre 0.0 y 100.0.
    """
    lista_filtrada = []

    for dato in lista_datos:
        if dato >= 0.0 and dato <= 100.0:
            lista_filtrada.append(dato)

    return lista_filtrada


def calcular_alertas(lista_filtrada, umbral_critico):
    """
    Recibe una lista filtrada de lecturas y un umbral crítico.
    Devuelve el total de lecturas menores al umbral.
    """
    total_alertas = 0

    for lectura in lista_filtrada:
        if lectura < umbral_critico:
            total_alertas = total_alertas + 1

    return total_alertas


def generar_log_sistema(total_alertas):
    """
    Recibe el total de alertas críticas y genera un mensaje del sistema
    indicando la plataforma y la acción correspondiente.
    """
    sistema = sys.platform

    if total_alertas > 3:
        accion = "ABORTAR"
    else:
        accion = "PERMITIDA"

    log = "[SISTEMA " + sistema + "] Alertas críticas encontradas: " + str(total_alertas) + ". Acción: " + accion

    return log


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

if __name__ == "__main__":

    lecturas_raw = [12.5, -5.0, 88.2, 120.1, 1.2, 0.0, 45.6, 2.5]
    UMBRAL = 3.0

    print("=== SISTEMA DE TELEMETRÍA DE AGENTE AUTÓNOMO ===\n")

    lecturas_limpias = limpiar_lecturas(lecturas_raw)
    alertas = calcular_alertas(lecturas_limpias, UMBRAL)
    log_final = generar_log_sistema(alertas)

    print("Lecturas originales:", lecturas_raw)
    print("Lecturas limpias:", lecturas_limpias)
    print(log_final)


"""
EVIDENCIAS DE CONTROL DE CALIDAD

1. PROMPT UTILIZADO

Actúa como un programador experto en Python Estructurado. Escribe el código de una función llamada limpiar_lecturas.
Recibe como parámetro una lista de números flotantes que representan distancias detectadas por un LIDAR y debe retornar
una nueva lista con solo los valores válidos entre 0.0 y 100.0.
Restricciones estrictas:
1. No utilices programación orientada a objetos.
2. No utilices manejo de excepciones, nada de bloques try-except.
3. Gestiona los errores usando condicionales if/else tradicionales.
4. Incluye un docstring descriptivo.
5. Usa estructuras básicas como for, if y append.

2. TABLA DE PRUEBAS DE ESCRITORIO MANUAL

Caso de prueba diferente:

lecturas_raw = [-10.0, 150.0, 200.0, -1.5]
UMBRAL = 3.0

1:
En la variable de lecturas_raw guardamos 4 datos.

2:
Se llama limpiar_lecturas(lecturas_raw).
Esta función revisa los datos, verifica y descarta:
-10.0
150.0
200.0 
-1.5

Resultado:
lecturas_limpias = []

3:
Se llama a calcular_alertas(lecturas_limpias, UMBRAL).
La lista esta vacia asi que no tiene nada que revisar

Resultado:

alertas = 0

4:
llamamos a generar_log_sistema(alertas).
Como alertas vale 0 y no es mayor que 3, la acción se marca como permitida.

Resultado:
[SISTEMA win32] Alertas críticas encontradas: 0. Acción: PERMITIDA


3. AUDITORÍA DE CÓDIGO

Si intento agregar funciones aun no vistas en clases, pero lo soluciones pidiendo que utilizara python basico 
"""