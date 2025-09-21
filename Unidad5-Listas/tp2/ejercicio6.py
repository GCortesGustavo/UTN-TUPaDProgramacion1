numeros :list = [1,2,3,4,5,6,7]

ultima_posicion = numeros[-1]

for i in range(len(numeros)-1, 0, -1):
    numeros[i] = numeros[i-1]

numeros[0] = ultima_posicion

print('Lista rotada', numeros)