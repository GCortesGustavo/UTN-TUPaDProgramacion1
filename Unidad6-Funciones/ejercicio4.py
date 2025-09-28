from math import pi

def calcular_area_circulo(radio):
    return pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio
    
    
def main():
    radio = float(input('Introduzca el radio del círculo: '))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f'El area del círculo es: {area}')
    print(f'El perimetro del círculo es: {perimetro}')

main()