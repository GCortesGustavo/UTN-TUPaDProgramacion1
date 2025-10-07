original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Perú": "Lima", "Brasil": "Brasilia"}

invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

print(f"Diccionario Original: {original}")
print(f"Diccionario Invertido: {invertido}")