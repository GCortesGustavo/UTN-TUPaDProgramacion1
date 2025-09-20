import random

numeros :list = []

for i in range(15):
    numeros.append(random.randint(1,100))

pares :list = []
impares :list = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)


print("Lista original:", numeros)
print("Pares:", pares, "Cantidad:", len(pares))
print("Impares:", impares, "Cantidad:", len(impares))
