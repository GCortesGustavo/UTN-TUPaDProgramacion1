# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

notas :list = [4, 8, 9, 10, 6, 4, 7, 2, 6, 9]
suma_total_notas :int = 0
nota_mas_alta :int = 0
nota_mas_baja :int = 11

for i in range(len(notas)):
    suma_total_notas += notas[i]

    if notas[i] > nota_mas_alta:
        nota_mas_alta = notas[i]
    
    if notas[i] < nota_mas_baja:
        nota_mas_baja = notas[i]

cantidad_notas = len(notas)
promedio :float =  suma_total_notas / cantidad_notas

print('Las notas de los estudiantes son:', notas)
print('La suma total de las notas es:', suma_total_notas)
print('La cantindad de notas es: ', cantidad_notas)
print('El promedio de las notas es:', promedio)
print('La nota mas baja es:', nota_mas_baja)
print('La nota mas alta es:', nota_mas_alta)