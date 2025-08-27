

palabra: str = 'PYTHON'
guiones: str = '_' * len(palabra)

vidas_totales: int = 6
letras_usadas: str = ""

while vidas_totales > 0 and "_" in guiones:
    print("Palabra actual: ", guiones)
    print("Vidas restantes: ", vidas_totales)
    print("Letras usadas: ", letras_usadas , " ")

    letra: str = input('Ingresa una letra para adivinar el ahorcado: ').upper()
    
    if len(letra) != 1 or not letra.isalpha():
        print('Letra Inválida')
        continue
    
    if letra in letras_usadas:
        print('Ya has utilizado esta letra')
        continue
    else: 
        letras_usadas += letra

    if letra in palabra:
        print('Acertaste!')
        nuevo_ingreso = ""
        for i in range (len(palabra)):
            if palabra[i] == letra:
                nuevo_ingreso += letra
            else:
                nuevo_ingreso += guiones[i]
        guiones = nuevo_ingreso
    else:
        print('Esa letra no esta en la palabra')
        vidas_totales -= 1

print('Game Over')
if "_" not in guiones:
    print("Ganaste")
else:
    print("Perdiste")