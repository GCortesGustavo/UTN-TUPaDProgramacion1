guia_telefonica = {}

bandera :bool = True

while bandera:
    contacto :str = input('Introduce el nombre del contacto: ')
    numero_telefonico :int = int(input('Introduce el número telefónico: '))


    guia_telefonica[contacto] = numero_telefonico

    if len(guia_telefonica) == 5: 
        bandera = False
    

print('La guía telefonica es: ', guia_telefonica)

consulta: str = input('Introduce el nombre para consultar su número: ')

if consulta in guia_telefonica:
    print(f'El número de {consulta} es {guia_telefonica[consulta]}')
else:
    print('El contacto no existe en la guía')



