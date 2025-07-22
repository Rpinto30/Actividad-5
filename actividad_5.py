sales = [20,1,55,236,1,-1]

while True:
    print("-"*10+"Bienvenido!"+"-"*10)
    print("  1. Ingresar lista de ventas\n  2. Mostrar todas las ventas ingresadas\n  3. Calcular la venta más alta y la más baja"+
          "\n  4. Calcular promedio de ventas\n  5. Contar cuántos días superaron los Q1000"+
          "\n  6. Clasificar cada venta\n  7. Salir")
    op = input("Ingrese una de las opciones: ")

    match op:
        case '1':
            days = int(input("\n>Ingrese la cantidad de dias que desea ingresar: "))
            for i in range(days+1):
                sale = int(input(f"Ingrese las ventas del días {i+1}: "))
                sales.append(sale)
            print("\nTodas las ventas han sido agregadas correctamente!")
        case '2':
            print("-"*10+"Ventas ingresadas: ")
            for i,j in enumerate(sales): print(f"{i+1})  {j}")
        case '3':
            mayor = sales[0]
            minus = sales[0]
            for i in sales:
                if i > mayor: mayor = i
                if i < minus: minus = i

            print(f"\nLa venta mayor resitrada es: {mayor}")
            print(f"\nLa venta menor resitrada es: {minus}")

        case _: print("Lo siento, no seleccionó ninguna opción, intente de nuevo")