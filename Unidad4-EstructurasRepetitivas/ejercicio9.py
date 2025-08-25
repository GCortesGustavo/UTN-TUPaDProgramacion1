# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

num_max: int = 100
suma: int = 0
media: float = 0

for i in range(1, num_max + 1):
    num:int = int(input(f'Ingrese el número {i}: '))
    suma = suma + num
    media = suma / num_max

print('La suma de todos los números es: ', suma)
print('La media de los números es: ', media)