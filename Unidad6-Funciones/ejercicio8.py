def calcular_imc(peso: float, altura: float):
    return peso / (altura ** 2)

def main():
    kilogramos = float(input('Introduzca su peso en kilogramos: '))
    altura = float(input('Introduzca su altura en metros: '))
    imc = calcular_imc(kilogramos, altura)
    print(f'El IMC es: {imc:.2f}')

main()