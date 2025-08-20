hemisferio = input('Ingrese el hemisferio (Norte/Sur): ')
mes = input('Escriba el mes del año: ')
dia = int(input('Ingrese qué día es: '))

if hemisferio.lower() == 'norte':
    if (mes.lower() == 'diciembre' and dia >= 21 ) or (mes.lower() == 'enero') or (mes.lower() == 'febrero') or (mes.lower() == 'marzo' and dia <= 20):
        print('Usted se encuentra en invierno')
    elif (mes.lower() == 'marzo' and dia >= 21) or (mes.lower() == 'abril') or (mes.lower() == 'mayo') or (mes.lower() == 'junio' and dia <=20):
        print('Usted se encuentra en primavera')
    elif (mes.lower() == 'junio' and dia >= 21) or (mes.lower() == 'julio') or (mes.lower() == 'agosto') or (mes.lower() == 'septiembre' and dia <=20):
        print('Usted se encuentra en verano')
    elif (mes.lower() == 'septiembre' and dia >= 21) or (mes.lower() == 'octubre') or (mes.lower() == 'noviembre') or (mes.lower() == 'diciembre' and dia <=20):
        print('Usted se encuentra en otoño')
elif hemisferio.lower() == 'sur':
    if (mes.lower() == 'diciembre' and dia >= 21 ) or (mes.lower() == 'enero') or (mes.lower() == 'febrero') or (mes.lower() == 'marzo' and dia <= 20):
        print('Usted se encuentra en verano')
    elif (mes.lower() == 'marzo' and dia >= 21) or (mes.lower() == 'abril') or (mes.lower() == 'mayo') or (mes.lower() == 'junio' and dia <=20):
        print('Usted se encuentra en otoño')
    elif (mes.lower() == 'junio' and dia >= 21) or (mes.lower() == 'julio') or (mes.lower() == 'agosto') or (mes.lower() == 'septiembre' and dia <=20):
        print('Usted se encuentra en invierno')
    elif (mes.lower() == 'septiembre' and dia >= 21) or (mes.lower() == 'octubre') or (mes.lower() == 'noviembre') or (mes.lower() == 'diciembre' and dia <=20):
        print('Usted se encuentra en primavera')