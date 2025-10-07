print("\n--- Ejercicio 7 (Corregido): Aprobados en parciales ---")

# El número sería su ID
parcial1_aprobados = {101, 105, 110, 115, 120}
parcial2_aprobados = {105, 112, 115, 121, 125}

print(f"IDs de aprobados en Parcial 1: {parcial1_aprobados}")
print(f"IDs de aprobados en Parcial 2: {parcial2_aprobados}\n")

aprobaron_ambos = parcial1_aprobados.intersection(parcial2_aprobados)
print(f"Estudiantes (ID) que aprobaron ambos parciales: {aprobaron_ambos}")

aprobaron_solo_uno = parcial1_aprobados.symmetric_difference(parcial2_aprobados)
print(f"Estudiantes (ID) que aprobaron solo uno de los dos parciales: {aprobaron_solo_uno}")

lista_total = parcial1_aprobados.union(parcial2_aprobados)
print(f"Lista total de estudiantes (ID) que aprobaron al menos un parcial: {lista_total}")