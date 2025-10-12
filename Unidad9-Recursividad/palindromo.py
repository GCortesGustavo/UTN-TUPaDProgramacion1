def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False
        
    sub_palabra = palabra[1:-1]
    return es_palindromo(sub_palabra)

palabra_usuario = input('Ingresa una palabra para verificar si es un palíndromo: ').lower().strip()

es_un_palindromo = es_palindromo(palabra_usuario)


if es_un_palindromo:
    print(f"La palabra '{palabra_usuario}' sí es un palíndromo")
else:
    print(f"La palabra '{palabra_usuario}' no es un palíndromo.")