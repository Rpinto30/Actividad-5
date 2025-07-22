sales = []

while True:
    print("-"*10+"Bienvenido!"+"-"*10)
    print("  1. Ingresar lista de ventas\n  2. Mostrar todas las ventas ingresadas\n  3. Calcular la venta más alta y la más baja"+
          "\n  4. Calcular promedio de ventas\n  5. Contar cuántos días superaron los Q1000\n  6. Buscar venta"+
          "\n  7. Clasificar cada venta\n  8. Salir")
    op = input("Ingrese una de las opciones: ")

    match op:
        case '1':
            days = int(input("\n>Ingrese la cantidad de dias que desea ingresar: "))
            for i in range(days+1):
                sale = int(input(f"Ingrese las ventas del días {i+1}: "))
                sales.append(sale)

        case _: print("Lo siento, no seleccionó ninguna opción, intente de nuevo")