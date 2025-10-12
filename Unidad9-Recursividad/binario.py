def decimal_a_binario(num):
    if num == 0:
        return ''
    else:
        cociente = num // 2

        residuo = num % 2

        return decimal_a_binario(cociente) + str(residuo)
    

numero_decimal = int(input('Ingrese un numero para pasarlo a binario: '))

resultado= decimal_a_binario(numero_decimal)

print(f'El binario de {numero_decimal} es: {resultado}')