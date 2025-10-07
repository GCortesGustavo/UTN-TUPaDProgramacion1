frase_usuario = input('Ingresa una frase: ')

frase_dividida = frase_usuario.split()

palabras_unicas = set(frase_dividida)
print(f'Las palabras únicas son: {palabras_unicas}')

recuento = {}
for palabra in frase_dividida:
    recuento[palabra] = recuento.get(palabra, 0) + 1 

print(f'recuento: {recuento}')