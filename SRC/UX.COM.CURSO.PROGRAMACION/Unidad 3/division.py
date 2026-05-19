def division_entera(dividendo, divisor):
    if divisor == 0:
        return "ERROR, Esta division no es posible"
    
    
    cociente = 0
    resto = dividendo

    while resto >= divisor:
        resto = resto - divisor    
        cociente = cociente + 1    

    return cociente, resto

dividendo = int(input("Ingresa el dividendo: "))
divisor   = int(input("Ingresa el divisor: "))

cociente, resto = division_entera(dividendo, divisor)
print(f"{dividendo} ÷ {divisor} = {cociente}, resto: {resto}")

def main():
    division_entera(dividendo, divisor)

if __name__ == "__main__":
    main()