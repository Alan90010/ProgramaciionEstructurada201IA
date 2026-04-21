def romano(num):
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    
    romano = ""
    
    for valor, simbolo in valores:
        while num >= valor:
            romano += simbolo
            num -= valor
            
    return romano

numero = int(input("Numero (1-3000): "))

if 1 <= numero <= 3000:
    print("Romano:", romano(numero))
else:
    print("Este numero es mayor a 3000")