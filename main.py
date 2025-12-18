import random

def generar_tablero(filas, columnas, minas):
    # Crear tablero vacío
    tablero = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Plantar minas de forma aleatoria
    minas_colocadas = 0
    while minas_colocadas < minas:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        if tablero[fila][columna] != -1:
            tablero[fila][columna] = -1
            minas_colocadas += 1

            # Incrementar conteo de minas en las celdas adyacentes
            for i in range(fila - 1, fila + 2):
                for j in range(columna - 1, columna + 2):
                    if 0 <= i < filas and 0 <= j < columnas and tablero[i][j] != -1:
                        tablero[i][j] += 1

    return tablero

# Ejemplo de uso
if __name__ == "__main__":
    filas, columnas, minas = 5, 5, 5  # Definición del tablero (5x5) con 5 minas
    tablero = generar_tablero(filas, columnas, minas)
    for fila in tablero:
        print(" ".join(str(celda) if celda != -1 else "*" for celda in fila)))