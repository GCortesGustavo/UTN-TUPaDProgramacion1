notas = [
    [7, 8, 6],
    [5, 9, 4],
    [10, 7, 8],
    [6, 6, 7],
    [9, 8, 10]
]

# Promedio de cada estudiante
for i in range(5):
    suma = 0
    for j in range(3):
        suma += notas[i][j]
    promedio = suma / 3
    print("Promedio del estudiante", i+1, ":", promedio)

# Promedio de cada materia
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
    promedio = suma / 5
    print("Promedio de la materia", j+1, ":", promedio)
