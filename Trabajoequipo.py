def mostrar_matriz(matriz):
    print("Plan de cobro")
    print("*" * 50)
    print("       ", end="")
    for mes in range(1, len(matriz[0]) + 1):
        print(f"{mes:>5}", end="")
    print()
    for i, fila in enumerate(matriz):
        print(f"Departamento {i + 1:<2}", end="")
        for valor in fila:
            print(f"{valor:>5.1f}", end="")
        print()
    print("*" * 50)


def ingresar_cobros(matriz, valores_uf):
    for i in range(len(matriz)):
        print(f"\nDepartamento {i + 1}")
        for j in range(len(matriz[i])):
            while True:
                try:
                    valor = float(input(f"Ingrese cantidad de UF a cobrar en el mes {j + 1}: "))
                    if 2 <= valor <= 5:
                        matriz[i][j] = valor
                        break
                    else:
                        print("Error, la cantidad de UF a cobrar debe estar entre 2 y 5.")
                except ValueError:
                    print("Entrada inválida. Intente nuevamente.")
        while True:
            try:
                valor_uf = float(input("Ingrese el valor promedio de la UF por los meses a cobrar: "))
                valores_uf[i] = valor_uf
                break
            except ValueError:
                print("Entrada inválida. Intente nuevamente.")


def total_por_departamento(matriz, valores_uf):
    depto = int(input("Ingrese el departamento a calcular y visualizar: "))
    if 1 <= depto <= len(matriz):
        total = 0
        print()
        for i, valor in enumerate(matriz[depto - 1]):
            cobro = valor * valores_uf[depto - 1]
            print(f"Departamento {depto}, mes {i + 1}: {valor:.1f} UF para un total a cobrar de $: {int(cobro)}")
            total += cobro
        print(f"Total cobro del departamento {depto} $: {int(total)}")
    else:
        print("Departamento no válido.")


def total_por_mes(matriz, valores_uf):
    mes = int(input("Ingrese el mes a calcular y visualizar: "))
    if 1 <= mes <= len(matriz[0]):
        total = 0
        print()
        for i in range(len(matriz)):
            valor = matriz[i][mes - 1]
            cobro = valor * valores_uf[i]
            print(f"Departamento {i + 1}, mes {mes}: {valor:.1f} UF para un total a cobrar de $: {int(cobro)}")
            total += cobro
        print(f"Total cobro del mes {mes} $: {int(total)}")
    else:
        print("Mes no válido.")

matriz = []
valores_uf = []
departamentos = 0
meses = 0

print("SISTEMA DE PLANIFICACIÓN DE COBRO DE GASTOS COMUNES")

while True:
    print("\n1. Generar plan de cobro")
    print("2. Ingresar cantidad y cobro de gasto común por departamento y mes")
    print("3. Visualizar el cobro total de un departamento en específico")
    print("4. Visualizar el cobro total de todos los departamentos en un mes específico")
    print("5. Salir del programa")

    opcion = input("\nSeleccione su opción: ")

    if opcion == "1":
        try:
            departamentos = int(input("Ingrese número de departamentos: "))
            meses = int(input("Ingrese número de meses de cobro: "))
            matriz = [[0.0 for _ in range(meses)] for _ in range(departamentos)]
            valores_uf = [0.0 for _ in range(departamentos)]
            mostrar_matriz(matriz)
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
    elif opcion == "2":
        if matriz:
            ingresar_cobros(matriz, valores_uf)
            mostrar_matriz(matriz)
        else:
            print("Primero debe generar el plan de cobro (opción 1).")
    elif opcion == "3":
        if matriz:
            total_por_departamento(matriz, valores_uf)
        else:
            print("Primero debe ingresar cobros (opción 2).")
    elif opcion == "4":
        if matriz:
            total_por_mes(matriz, valores_uf)
        else:
            print("Primero debe ingresar cobros (opción 2).")
    elif opcion == "5":
        print("Fin de la ejecución del programa")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
