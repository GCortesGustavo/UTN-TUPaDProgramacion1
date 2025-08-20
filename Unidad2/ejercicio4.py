edad = int(input('Ingrese su edad: '))

if edad < 12:
    print('Pertenece a la categoría Niño/a')
elif 12 <= edad < 18:
    print('Pertenece a la categoría Adolescente')
elif 18 <= edad < 30:
    print('Pertenece a la categoría Adulto/a joven')
elif edad >= 30:
    print('Pertenece a la categoría Adulto/a')
