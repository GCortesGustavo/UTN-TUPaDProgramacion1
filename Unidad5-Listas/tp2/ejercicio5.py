nombres :list = ["Facundo", "Jorge", "Santiago", "Leonardo", "Gustavo", "Luciano", "Nahuel", "Andres"]

print('Presione 1 para agregar un nuevo estudiante, 2 para eliminar')
opcion_usuario :int = int(input('Mi opción es: '))

if opcion_usuario == 1:
    nuevo_nombre = input('El nuevo nombre es: ')
    nombres.append(nuevo_nombre)
else:
    nombre_eliminado = input('El nombre eliminado es: ')
    if nombre_eliminado in nombres:
        nombres.remove(nombre_eliminado)
    else:
        print('El nombre no se encuentra en la lista')


print('La lista final es: ', nombres)