def contar_bloques(n):
    if n <= 0:
        return 0

    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


bloques_base = int(input("Ingrese el número de bloques en el nivel más bajo de la pirámide: "))
    
total = contar_bloques(bloques_base)
    
print(f"Para construir una pirámide con {bloques_base} bloques en la base, se necesitan un total de {total} bloques.")
