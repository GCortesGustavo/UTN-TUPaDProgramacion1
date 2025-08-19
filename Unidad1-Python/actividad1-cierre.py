# Ejercicio 1: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print('***Actividad 1***')
print('Hola mundo')

# Ejercicio 2:  Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
print('***Actividad 2***')
nombre = input('Por favor, escriba su nombre: ')
print('Hola',nombre + "!")

# Ejercicio 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
print('***Actividad 3***')
nombre = input('Por favor, escriba su nombre: ')
apellido = input('Por favor, escriba su apellido: ')
edad = int(input('Por favor, indique su edad: '))
residencia = input('Por favor, indique su lugar de residencia: ')
print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.'
print('***Actividad 4***')
radio = float(input("Indique el radio de un círculo: "))
area = 3.14 * (radio**2)
print("El área del circulo es: ", area)
perimetro = 2 * 3.14 * radio
print('El perímetro del circulo es: ', perimetro)


# Ejercicio 5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
print('***Actividad 5***')
segundos = int(input('Escriba una cantidad de segundos para obtener la equivalencia en horas: '))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")


# Ejercicio 6:Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
print('***Actividad 6***')
numero = int(input('Indique un número: '))
print(f'multiplicamos 1 x {numero}:', numero * 1)
print(f'multiplicamos 2 x {numero}:', numero * 2)
print(f'multiplicamos 3 x {numero}:', numero * 3)
print(f'multiplicamos 4 x {numero}:', numero * 4)
print(f'multiplicamos 5 x {numero}:', numero * 5)
print(f'multiplicamos 6 x {numero}:', numero * 6)
print(f'multiplicamos 7 x {numero}:', numero * 7)
print(f'multiplicamos 8 x {numero}:', numero * 8)
print(f'multiplicamos 9 x {numero}:', numero * 9)
print(f'multiplicamos 10 x {numero}:', numero * 10)

# Ejercicio 7:Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print('***Actividad 7***')
numero1 = int(input('Indique el primer número distinto de cero: '))
numero2 = int(input('Indique el segundo número distinto de cero: '))
suma = numero1 + numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
resta = numero1 - numero2 

print(f'El resultado de la suma entre {numero1} y {numero2} es: ', suma)
print(f'El resultado de la divisón entre {numero1} y {numero2} es: ', division)
print(f'El resultado de la multiplicación entre {numero1} y {numero2} es: ', multiplicacion)
print(f'El resultado de la resta entre {numero1} y {numero2} es: ', resta)

# Ejercicio 8:Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo: IMC = peso en kg / (altura en m)^2
print('***Actividad 8***')
altura = float(input('Indique su altura: '))
peso = float(input('Indique su peso: '))
print('Su altura es: ', altura, 'm')
print('Su peso es: ', peso, 'kg')
imc = peso / (altura ** 2)
print('Su índice de masa corporal es de: ', imc)

# Ejercicio 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: Temperatura en Fahrenheit = 9/5. Temperatura en Celcius + 32
print('***Actividad 9***')
grados_celsius = float(input('Indique los grados celsius para obtener su equivalencia en Fahrenheit: '))
temperatura_fahrenheit = (grados_celsius * 1.8) + 32
print('El equivalente en Fahrenheit es: ', temperatura_fahrenheit, 'F')

# Ejercicio 10: Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
print('***Actividad 10***')
numero1 = int(input('Indique el primer número: '))
numero2 = int(input('Indique el segundo número: '))
numero3 = int(input('Indique el tercer número: '))

promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio entre {numero1}, {numero2} y {numero3} es: ", promedio)



