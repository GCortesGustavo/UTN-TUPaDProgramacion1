alumnos :set= {}
numero_alumnos = 3

for i in range(numero_alumnos):
    nombre = input(f'Ingrese el nombre del alumno {i + 1}: ')

    nota1 = float(input(f'La nota 1 para {nombre}: '))
    nota2 = float(input(f'La nota 2 para {nombre}: '))
    nota3 = float(input(f'La nota 3 para {nombre}: '))

    alumnos[nombre] = (nota1, nota2, nota3)


for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)

    print(f"El promedio de {nombre} es: {promedio:.2f}")