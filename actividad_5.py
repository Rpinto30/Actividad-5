sales = []

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
                while True:
                    sale = int(input(f"Ingrese las ventas del días {i+1}: "))
                    if sale > 0: break
                    else: print("\nLo siento, numero negativo, intente de nuevo")
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
        case '4':
            print(f"\n El promedio de ventas hasta el momento es: {sum(sales)/len(sales)}")
        case '5':
            days_1000 = 0
            for i in sales:
                if i > 1000: days_1000+=1
            print(f"\nLos días que superaron los Q1000 son {days_1000}")
        case '6':
            print("---Clasificación de ventas---")
            for i in sales:
                if i > 1000: print(f"Venta: {i}  Alta")
                elif i >= 500: print(f"Venta: {i}  Media")
                else: print(f"Venta: {i}  Baja")

        case '7':
            print("\nNos vemos")
        case _: print("Lo siento, no seleccionó ninguna opción, intente de nuevo")