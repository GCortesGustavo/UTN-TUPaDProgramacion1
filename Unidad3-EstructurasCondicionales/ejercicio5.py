contrasena: str = input('Ingrese su contraseña: ')

if 8 <= len(contrasena) <=18:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')