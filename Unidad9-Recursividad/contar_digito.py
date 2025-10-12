def contar_digito(numero, digito):
    if numero == 0:
        return 0

    ultimo_digito = numero % 10
    resto_del_numero = numero // 10
    
    if ultimo_digito == digito:
        return 1 + contar_digito(resto_del_numero, digito)
    else:
        return contar_digito(resto_del_numero, digito)


num_entero = int(input("Ingrese un número entero positivo: "))
dig_a_buscar = int(input("Ingrese el dígito (0-9) que desea contar: "))

cantidad = contar_digito(num_entero, dig_a_buscar)
        
print(f"El dígito {dig_a_buscar} aparece {cantidad} veces en el número {num_entero}.")
