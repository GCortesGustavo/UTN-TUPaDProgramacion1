def potencia(num, exponente):
    if exponente == 0:
        return 1
    if num == 0:
        return 1
    else:
        return num * potencia(num, exponente - 1)
    

numero = int(input('Escriba un número base: '))
exponente = int(input('Escriba el exponente: '))

print(potencia(numero, exponente))