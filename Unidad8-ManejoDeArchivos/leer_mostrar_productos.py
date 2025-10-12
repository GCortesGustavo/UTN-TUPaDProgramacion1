# def leer_mostrar_productos():
#     with open('productos.txt', 'r', encoding='utf-8') as archivo:
#         lineas = archivo.readlines()

#     print("\n--- Productos actuales ---")
    
#     for linea in lineas[1:]:
#         if linea.strip():
#             nombre, precio, cantidad = linea.strip().split(',')
#             print(f'Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}')

#     print("\n--- Agregar nuevo producto ---")
#     nuevo_nombre = input("Nombre: ")
#     nuevo_precio = input("Precio: ")
#     nueva_cantidad = input("Cantidad: ")

#     with open('productos.txt', 'a', encoding='utf-8') as archivo:
#         archivo.write(f'{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n')

#     print(f"\nProducto agregado: {nuevo_nombre} | Precio: ${nuevo_precio} | Cantidad: {nueva_cantidad}")

# leer_mostrar_productos()

def cargar_productos():
    productos = []
    with open('productos.txt', 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        
        for linea in lineas[1:]:
            if linea.strip(): 
                nombre, precio, cantidad = linea.strip().split(',')
                
                producto_dic = {
                    'nombre': nombre,
                    'precio': float(precio), 
                    'cantidad': int(cantidad)
                }
                productos.append(producto_dic)
    print("Productos cargados.")
    return productos

def guardar_productos(lista_productos):
    with open('productos.txt', 'w', encoding='utf-8') as archivo:
        archivo.write('nombre,precio,cantidad\n')
        
        for producto in lista_productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print(f"Productos guardados en el archivo.")

lista_de_productos = cargar_productos()

print("Productos actuales")
for p in lista_de_productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

print("Buscar producto")
nombre_a_buscar = input("Ingresa el nombre del producto que deseas buscar: ")

encontrado = False
for producto in lista_de_productos:
    if producto['nombre'].lower() == nombre_a_buscar.lower():
        print("\n¡Producto encontrado!")
        print(f"  Nombre: {producto['nombre']}")
        print(f"  Precio: ${producto['precio']}")
        print(f"  Cantidad: {producto['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print(f"El producto '{nombre_a_buscar}' no se encuentra en la lista.")

print("\n--- Agregar nuevo producto ---")
nuevo_nombre = input("Nombre: ")
nuevo_precio = float(input("Precio: ")) 
nueva_cantidad = int(input("Cantidad: "))  

nuevo_producto_dic = {
    'nombre': nuevo_nombre,
    'precio': nuevo_precio,
    'cantidad': nueva_cantidad
}

lista_de_productos.append(nuevo_producto_dic)
print(f"Producto '{nuevo_nombre}' agregado a la lista en memoria.")

guardar_productos(lista_de_productos)