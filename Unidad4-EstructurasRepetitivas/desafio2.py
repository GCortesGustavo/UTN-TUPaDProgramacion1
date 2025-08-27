import random

print('Piedra, papel o tijeras')
print('El primero en ganar 3 rondas es el ganador')
print('1- Piedra \n2- Papel \n3- Tijeras')

puntos_jugador: int = 0
puntos_pc: int = 0
ronda:int = 1

while puntos_jugador < 3 and puntos_pc < 3:
    print(f'---Primera ronda {ronda}---')

    eleccion_jugador: int = int(input('Elige tu opcion (1= Piedra, 2= Papel o 3= Tijeras): '))
    
    if eleccion_jugador < 1 or eleccion_jugador > 3:
        print('Opcion incorrecta, elige 1, 2 o 3')
        continue

    eleccion_pc: int = random.randint(1,3)

    print(f'Elegiste {eleccion_jugador} y la pc eligio {eleccion_pc}')

    if eleccion_jugador == eleccion_pc:
        print('Empate!')
    elif (eleccion_jugador == 1 and eleccion_pc == 3) or \
        (eleccion_jugador == 2 and eleccion_pc == 1) or \
        (eleccion_jugador == 3 and eleccion_pc == 2):
        print('Ganaste')
        puntos_jugador += 1
    else: 
        print('Perdiste :c')
        puntos_pc += 1

    print(f'Marcador --> Jugador:{puntos_jugador} | PC: {puntos_pc}')
    ronda += 1

print('=== Fin del Juego===')
if puntos_jugador > puntos_pc:
    print('Ganaste la partida')
else:
    print('Perdiste la partida :c')