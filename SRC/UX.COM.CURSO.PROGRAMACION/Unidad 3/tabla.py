def tabla(n):
    print("     ", end="")
    for i in range(1, n+1):
        print(f"{i:4}", end="")
    print()
    
    print("    " + "----" * n) 
    
    for fila in range(1, n+1):
        print(f"{fila:2} *", end="")  
        for col in range(1, n+1):
            print(f"{fila*col:4}", end="")
        print() 

def main():
    limite = int(input("Ingrese hasta donde llegara la tabla: "))
    tabla(limite)


if __name__ == "__main__":
    main()