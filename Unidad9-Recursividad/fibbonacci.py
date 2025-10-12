def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    
numero = int(input('Escribe un número: '))

for i in range(1, numero + 1):
    resultado = fibonacci(i)
    print(f'El valor de fibo en {i} es: {resultado}')

print(fibonacci(numero))