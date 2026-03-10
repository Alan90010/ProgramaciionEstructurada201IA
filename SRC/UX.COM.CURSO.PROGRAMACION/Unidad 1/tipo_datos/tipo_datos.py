# Demostracion de tipo de datos

def datos():

    entero  = 25
    decimal = 3.14
    cadena  = "Hola, Mundo"
    boleano = True 

    print(entero)
    print(decimal)
    print(cadena)
    print(boleano)

def tipos_datos_compuestos():
    lista = [10, 20, 30, 40]
    tupla = [19, 29, 39, 49]
    diccionario = {"nombre": "Juan", "edad": 38, "ciudad": "Madrid"}

    print(lista)
    print(tupla)
    print(diccionario)


def main():
    datos()
    tipos_datos_compuestos()

if __name__ == "__main__":
    main()
