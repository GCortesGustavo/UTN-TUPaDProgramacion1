stock = {"manzana": 50, "banana": 30, "naranja": 45}

while True:
    print("\n--- Menú de Stock ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar stock o nuevo producto")
    print("3. Salir")
    opcion = input("Elegí una opción: ")

    if opcion == '1':
        producto = input("Ingresá el nombre del producto a consultar: ").lower()
        if producto in stock:
            print(f"El stock de {producto} es: {stock[producto]} unidades.")
        else:
            print(f"El producto '{producto}' no se encuentra en el stock.")
    
    elif opcion == '2':
        producto = input("Ingresá el nombre del producto: ").lower()
        cantidad = int(input("Ingresá la cantidad a agregar: "))
        
        if producto in stock:
            stock[producto] += cantidad
            print(f"Stock actualizado. Nuevo stock de {producto}: {stock[producto]}")
        else:
            stock[producto] = cantidad
            print(f"Nuevo producto '{producto}' agregado con un stock de {cantidad}.")

    elif opcion == '3':
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, intentá de nuevo.")