# Adivina el número - enunciado
import random

numero_random: int = random.randint(1,100)

max_intentos: int = 10
intentos: int = 0
numero: int = 0

print('Adivina el numero random entre 1 y 100')

while intentos != max_intentos and numero != numero_random:
    numero:int = int(input('Escribe un número: '))

    if numero > numero_random:
        print('---------')
        print('Mas chico')
        print('---------')
        intentos += 1

    if numero < numero_random:
        print('---------')
        print('Mas grande')
        print('---------')
        intentos += 1
    
    if numero == numero_random:
        intentos += 1
        print(f'Acertaste en {intentos} intentos!')
    
    if intentos == max_intentos:
        print('Te quedaste sin intentos.')






