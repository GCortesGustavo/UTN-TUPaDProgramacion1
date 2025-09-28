def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

def main():
    numero1 = int(input('Introduzca el primer número: '))
    numero2 = int(input('Introduzca el segundo número: '))
    suma, resta, mult, div = operaciones_basicas(numero1, numero2)
    print(f'Suma: {suma}')
    print(f'Resta: {resta}')
    print(f'Multiplicación: {mult}')
    print(f'División: {div}')

main()
