import math

def esfera():

    radio = float(input("Ingrese el radio de la esfera en cm: "))
    volumen = (4/3) * math.pi * math.pow(radio, 3)
    print ("El volumen de la esfera es: ", volumen, "cm cubicos")

def main():
    esfera()

if __name__ == "__main__":
    main()