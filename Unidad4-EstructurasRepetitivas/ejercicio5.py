# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

numero_aleatorio: int = random.randint(0, 9)
intentos: int = 0
numero_usuario: int = -1

print('Adivina el número entre 0 y 9')

while numero_usuario != numero_aleatorio:
    numero_usuario = int(input('Ingresa un número: '))
    intentos += 1
print(f'Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.')
