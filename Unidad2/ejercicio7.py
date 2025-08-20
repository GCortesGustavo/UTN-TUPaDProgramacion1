frase = input('Ingrese una frase o una palabra: ')

if frase[-1] == 'a' or frase[-1] == 'e' or frase[-1] == 'i' or frase[-1] == 'o' or frase[-1] == 'u':
    print(frase+'!')
else:
    print(frase)