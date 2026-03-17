import math

# Demostracion del uso de funciones de math

def mostrar_funciones_math(numero):
    # Crear una variable

    sen_x = math.sin(numero)
    cos_x = math.cos(numero)

    print(" El seno de", numero, "es", sen_x)
    print(" El cos de", numero, "es", cos_x)


    resultado = sen_x ** 2 + cos_x ** 2 

    print("El resultado de sen*2(x) + cos*2(x) =", resultado)

def mostrar_funciones_math_tan(numero):
    # Crear una variable

    tan_x = math.tan(numero)

    print(" El tan de", numero, "es", tan_x)

def main():
    numero = float(input("Ingrese un numero: "))
    mostrar_funciones_math(numero)
    mostrar_funciones_math_tan(numero)

if __name__ == "__main__":
    main()