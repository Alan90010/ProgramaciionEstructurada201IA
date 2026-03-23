def lotes():
    total = 0

    while True:

        lote = float(input("Cual es el tamaño del lote en MB? ")) 
        total = total + lote

        print("El tamaño es:", total ,"MB")

        if total > 2500:
            print("Out of Memory")
            print("El total no puede superar los 2500 MB")
            break

def main():
    lotes()

if __name__ == "__main__":
    main()