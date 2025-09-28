def calcular_promedio(a:float, b:float, c:float):
    return (a + b + c) / 3

def main():
    numero1 = float(input('Introduzca el primer número: '))
    numero2 = float(input('Introduzca el segundo número: '))
    numero3 = float(input('Introduzca el tercer número: '))
    promedio = calcular_promedio(numero1, numero2, numero3)

    print(f'El promedio entre {numero1}, {numero2}, {numero3} es: {promedio}')


main()