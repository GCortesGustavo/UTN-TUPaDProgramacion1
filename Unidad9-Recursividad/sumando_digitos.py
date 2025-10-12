def suma_digitos(n):
    if n < 10:
        return n
    else:
        ultimo_digito = n % 10
        
        resto_del_numero = n // 10
        
        return ultimo_digito + suma_digitos(resto_del_numero)



numero = int(input("Ingrese un número entero positivo: "))


resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")

