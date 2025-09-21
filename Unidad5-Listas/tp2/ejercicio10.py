ventas = [
    [10, 12, 15, 20, 18, 22, 19],  
    [5, 7, 9, 10, 8, 6, 12],       
    [14, 13, 16, 15, 20, 18, 17],  
    [9, 8, 7, 6, 5, 4, 10]         
]

for i in range(4):
    total = 0
    for j in range(7):
        total += ventas[i][j]
    print("Total producto", i+1, ":", total)

mayor_dia = -1
mayor_venta = -1
for j in range(7):
    suma = 0
    for i in range(4):
        suma += ventas[i][j]
    if suma > mayor_venta:
        mayor_venta = suma
        mayor_dia = j+1
print("Día con mayores ventas:", mayor_dia)

totales = []
for i in range(4):
    suma = 0
    for j in range(7):
        suma += ventas[i][j]
    totales.append(suma)

mas_vendido = max(totales)
producto = totales.index(mas_vendido) + 1
print("Producto más vendido en la semana: Producto", producto)
