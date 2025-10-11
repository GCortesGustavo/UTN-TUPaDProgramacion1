def leer_mostrar_productos():
    with open('productos.txt', 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    print("\n--- Productos actuales ---")
    
    for linea in lineas[1:]:
        if linea.strip():
            nombre, precio, cantidad = linea.strip().split(',')
            print(f'Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}')

    print("\n--- Agregar nuevo producto ---")
    nuevo_nombre = input("Nombre: ")
    nuevo_precio = input("Precio: ")
    nueva_cantidad = input("Cantidad: ")

    with open('productos.txt', 'a', encoding='utf-8') as archivo:
        archivo.write(f'{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n')

    print(f"\nProducto agregado: {nuevo_nombre} | Precio: ${nuevo_precio} | Cantidad: {nueva_cantidad}")

leer_mostrar_productos()