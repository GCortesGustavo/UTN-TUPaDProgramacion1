# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 8, 7]
print(max(numeros))

numeros.remove(max(numeros))
print(numeros)

# Lo que ocurre en este programa es que se elimina el primer número más grande de la lista. Es decir que en orden de índice,
# revisa y elimina el número con valor más alto.