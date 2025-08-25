# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num: int = int(input('Introduce un número entero: '))

contador: int = 0

while num > 0:
    num //= 10
    contador += 1

print('La cantidad de dígitos es: ', contador)