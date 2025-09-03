# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

bandera: bool = True

while bandera:
    numero = input('Ingrese un número entero: ')
    if numero.lstrip('-').isdigit():  
        num = abs(int(numero))       
        contador: int = 0
        if num == 0:
            contador = 1
        else:
            while num > 0:
                num //= 10
                contador += 1
        print('La cantidad de dígitos es:', contador)
        bandera = False
    else:
        print('Ingrese un valor válido')
        print('----------------------------------')