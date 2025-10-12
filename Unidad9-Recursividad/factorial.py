def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


numero = int(input('Escriba un numero: '))


for i in range(1, numero + 1):
    resultado = factorial(i)
    print(f'El factorial de {i} es :{resultado}')
