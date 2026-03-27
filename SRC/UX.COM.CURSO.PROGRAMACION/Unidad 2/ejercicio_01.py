"""
Diseñar un algoritmo que calcule la suma de
todos los numeros enteros del 1 al 100 que son
divisores por 3 Y, ademas, Impares
"""

def es_dividible():
    suma = 0
    i = 1
    while i <= 100:
        if i % 3 == 0 and i%2!=0:
            suma += i 
        i += 1
    return suma

def mian():
    suma = es_dividible()
    print(suma)

if __name__ == "__main__":
    mian()