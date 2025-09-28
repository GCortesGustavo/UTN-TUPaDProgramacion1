def saludar_usuario(nombre:str):
    print(f'Hola {nombre}!')

def main():
    usuario: str = input('Introduzca su nombre: ')
    saludar_usuario(usuario)

main()