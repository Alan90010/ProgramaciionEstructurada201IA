def impares():
    N = int(input("Ingrese cuantos numeros impares generar: "))

    contador = 0
    numero = 1

    while contador < N:

        print(numero)

        numero = numero + 2
        
        contador = contador + 1

def main():
    N = impares()
    print(N)

if __name__=="__main__":
    main()