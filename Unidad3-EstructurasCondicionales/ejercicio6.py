# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números.

import random
from statistics import mode, median, mean

numeros_aleatorios: int = [random.randint(1, 100) for _ in range(50)]

print("Números aleatorios:", numeros_aleatorios)
print("Moda:", mode(numeros_aleatorios))
print("Mediana:", median(numeros_aleatorios))
print("Media:", mean(numeros_aleatorios))