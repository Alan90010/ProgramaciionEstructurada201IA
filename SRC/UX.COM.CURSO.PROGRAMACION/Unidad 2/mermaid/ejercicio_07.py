def horastrabajo():
    total_acumulado = 0
    semanas = 0
    meta = 2500

    while total_acumulado < meta:
        salario = float(input("Ingrese el salario semanal: "))

        total_acumulado = total_acumulado + salario
        semanas = semanas + 1

    return semanas

def main():
    total_semanas = horastrabajo()
    print("Semanas Trabajadas", total_semanas)

if __name__ == "__main__":
    main()