lista :list = [4, 3 , 5 , 7, 80, 15, 40, 12, 20, 30, 10, 2]

# lista.sort()

for i in range(len(lista)):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print('La lista ordenada es: ', lista)