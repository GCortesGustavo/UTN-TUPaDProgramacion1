agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("jueves", "09:30"): "Cita con el dentista",
    ("viernes", "20:00"): "Cena con amigos"
}

dia = input("Ingresá el día a consultar (ej: lunes): ").lower()
hora = input("Ingresá la hora a consultar (formato HH:MM): ")

consulta = (dia, hora)

evento = agenda.get(consulta, "No hay ningún evento programado en esa fecha y hora.")

print(f"Resultado: {evento}")