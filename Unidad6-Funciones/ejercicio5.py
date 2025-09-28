def segundos_a_horas(segundos: int):
    return segundos / 3600

def main():
    segundos :int =int(input('Introduce los segundos para converti a horas: '))
    conversion :float = segundos_a_horas(segundos)
    print(f'{segundos} equivale a {conversion:.2f} hora/s')

main()