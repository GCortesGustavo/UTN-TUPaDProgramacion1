magnitud: float = float(input('Ingrese la magnitud del terremoto: '))

if magnitud < 0:
    print('Magnitud inválida')
elif magnitud < 3:
    print('Muy leve')
elif 3 <= magnitud <4:
    print('Leve')
elif 4 <= magnitud <5:
    print('Moderado')
elif 5 <= magnitud < 6:
    print('Fuerte')
elif 6 <= magnitud < 7:
    print('Muy Fuerte')
elif 7 <= magnitud:
    print('Extremo')