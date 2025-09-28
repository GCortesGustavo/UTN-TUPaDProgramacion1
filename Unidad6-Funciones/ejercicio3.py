def informacion_personal(nombre :str, apellido: str, edad:int, residencia: str):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.')

def main():
    nombre: str= input('Introduzca su nombre: ')
    apellido: str= input('Introduzca su apellido: ')
    edad: int= int(input('Introduzca su edad: '))
    residencia: str= input('Introduzca su residencia: ')
    informacion_personal(nombre, apellido, edad, residencia)

main()