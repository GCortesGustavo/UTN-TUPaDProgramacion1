nombre = input('Ingrese su nombre: ')

print('Hola, ' + nombre)

print('Seleccione una opción:')
print('1: Si quiere su nombre en mayúsculas')
print('2: Si quiere su nombre en minúscular')
print('3: Si quiere su primera letra en mayúscula')


opcion = int(input('Ingrese la opción deseada (1, 2 o 3): '))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
