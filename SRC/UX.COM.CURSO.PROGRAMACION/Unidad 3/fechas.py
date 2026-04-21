def bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def fecha_valida(dia, mes, año):
    if mes < 1 or mes > 12:
        return False

    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if bisiesto(año):
        dias_mes[1] = 29

    max_dias = dias_mes[mes - 1]

    return 1 <= dia <= max_dias

dia  = int(input("Ingresa el día: "))
mes  = int(input("Ingresa el mes: "))
año  = int(input("Ingresa el año: "))

if fecha_valida(dia, mes, año):
    print(f"{dia}/{mes}/{año} Valida")
else:
    print(f"{dia}/{mes}/{año} Invalida")

def main():
    bisiesto(año)
    fecha_valida(dia, mes, año)

if __name__ == "__main__":
    main()