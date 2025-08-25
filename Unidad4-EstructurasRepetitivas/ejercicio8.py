# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

numeros_negativos: int = 0
numeros_positivos: int = 0
numeros_pares: int = 0
numeros_impares: int = 0

num_max:int = 100

for i in range(1, num_max + 1):
    num: int = int(input('Ingresa el número: '))
    if num % 2 == 0:
        numeros_pares = numeros_pares + 1
    else:
        numeros_impares = numeros_impares + 1
    
    if num < 0:
        numeros_negativos = numeros_negativos + 1
    elif num > 0:
        numeros_positivos = numeros_positivos + 1

print('Los numeros pares son: ', numeros_pares)
print('Los numeros impares son: ', numeros_impares)
print('Los numeros positivos son: ', numeros_positivos)
print('Los numeros negativos son: ', numeros_negativos)
