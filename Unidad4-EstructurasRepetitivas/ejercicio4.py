# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

num: int = 1
suma: int = 0

while num != 0:
    num: int = int(input('Ingrese un número entero(0 para terminar): '))
    suma = suma + num
print('La suma total es: ', suma)