def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
    

def main():
    numero :int = int(input('Introduce un número para ver su tabla de multiplicar: '))
    tabla_multiplicar(numero)

main()