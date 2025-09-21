tablero = [["-","-","-"],
           ["-","-","-"],
           ["-","-","-"]]

for turno in range(9):  
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "O"
    
    print("Turno del jugador", jugador)
    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada, pierdes turno.")

    for f in tablero:
        print(f)
