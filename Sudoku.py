import random


# Se crea el tablero del sudoky 9 x 9
def generar_sudoku(tablero, pistas=25):
    if len(tablero) != 9 or any(len(fila) != 9 for fila in tablero):
        raise ValueError("El tablero debe ser de 9x9.")

# Creo las "pistas" que son los números iniciales que apareceran en el primer sudoku
    while pistas > 0:
        fila, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)

        if tablero[fila][col] == 0 and es_valido(tablero, fila, col, num):
            tablero[fila][col] = num
            pistas -= 1

# Con esta función evito que se escriba un número en una celda donde ya hay otro número
def es_valido(tablero, fila, col, num):
    if num in tablero[fila]:
        return False

    if num in [tablero[i][col] for i in range(9)]:
        return False

    cuadro_fila = (fila // 3) * 3
    cuadro_col = (col // 3) * 3
    for i in range(cuadro_fila, cuadro_fila + 3):
        for j in range(cuadro_col, cuadro_col + 3):
            if tablero[i][j] == num:
                return False

    return True

# Función para resolver el sudoku
def resolver_sudoku(tablero):
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:
                for num in range(1, 10):
                    if es_valido(tablero, fila, col, num):
                        tablero[fila][col] = num
                        if resolver_sudoku(tablero):
                            return True
                        tablero[fila][col] = 0
                return False
    return True

# Se imprime el sudoku
def imprimir_sudoku(tablero):
    for fila in tablero:
        print(" ".join(str(num) if num != 0 else "." for num in fila))

# Crear tablero inicial
tablero = [[0] * 9 for _ in range(9)]

# Selecciona 25 celdas donde poner números random
generar_sudoku(tablero, pistas=25)

# Mostrar el sudoku inicial en la consola
print("Sudoku inicial:")
imprimir_sudoku(tablero)

# Resuelve el sudoku
if resolver_sudoku(tablero):
    print("\nSudoku resuelto:")
    imprimir_sudoku(tablero)
else:
    print("No se pudo resolver el Sudoku.")
    

