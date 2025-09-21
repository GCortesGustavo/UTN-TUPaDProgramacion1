datos = [1,3,5,3,7,1,9,5,3]

lista_sin_repetidos = []

for i in datos:
    if i not in lista_sin_repetidos:
        lista_sin_repetidos.append(i)

print("Lista original:", datos)
print("Lista sin repetidos:", lista_sin_repetidos)
