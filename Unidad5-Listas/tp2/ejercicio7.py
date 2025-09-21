temperaturas = [
    [10, 20],
    [12, 22],
    [9, 18],
    [11, 25],
    [8, 21],
    [13, 23],
    [7, 19]
]

suma_min = 0
suma_max = 0
amplitudes = []

for dia in range(7):
    minimo = temperaturas[dia][0]
    maximo = temperaturas[dia][1]
    suma_min += minimo
    suma_max += maximo
    amplitudes.append(maximo - minimo)

prom_min = suma_min / 7
prom_max = suma_max / 7
mayor_amplitud = max(amplitudes)
dia_mayor = amplitudes.index(mayor_amplitud) + 1

print("Promedio de mínimas:", prom_min)
print("Promedio de máximas:", prom_max)
print("Mayor amplitud en el día:", dia_mayor)
