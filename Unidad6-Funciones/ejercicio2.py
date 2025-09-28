def saludar_usuario(nombre:str):
    return f'Hola {nombre}!'

def main():
    usuario: str = input('Introduzca su nombre: ')
    saludo:str = saludar_usuario(usuario)
    print(saludo)

main()