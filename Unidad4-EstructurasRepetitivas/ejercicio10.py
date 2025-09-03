# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero: str = input("Ingrese un número: ")
invertido = ""

if numero.startswith('-'):
    for i in range(len(numero) - 1, 0, -1):  # Empieza en len(numero)-1 y termina en 1
        invertido += numero[i]
    invertido = '-' + invertido
else:
    for i in range(len(numero) - 1, -1, -1):
        invertido += numero[i]

print("Número invertido:", invertido)

# Otra forma de hacerlo usando slicing
# numero: str = input("Ingrese un número: ")
# numero_invertido = numero[::-1]
# print("Número invertido:", numero_invertido)