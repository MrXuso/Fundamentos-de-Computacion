"""***************************************************
--- FRANCISCO JESÚS JIMÉNEZ HIDALGO                ---
--- FUNDAMENTOS DE PROGRAMACIÓN                    ---
--- Sopa de letras                                 ---
---************************************************"""

# palabra = input('Introduzca la palabra a buscar: ')
# filas = int(input('Introduzca el número de filas: '))
# columnas = int(input('Introduzca el número de columnas: '))
vectorDirecciones = [['E', 0, 1], ['O', 0, -1], ['S', 1, 0], ['N', -1, 0],
                     ['SE', 1, 1], ['SO', 1, -1], ['NE', -1, 1], ['NO', -1, -1]]


def buscarPalabra(tablero, palabra, filas, columnas, vectorDirecciones):
    """list[][], str -> str
    +++OBJ: busca la palabra en la sopa de letras
    +++PRE: tablero lista de string"""
    coincidencias = [0 for i in range(8)]

    for i in range(0, 8, 2):
        vectorDireccion = vectorDirecciones[i]

        """Veces que tenemos que buscar una palabra en una matriz filas x columnas"""
        veces = max([abs(vectorDireccion[1]) * filas, abs(vectorDireccion[2]) * columnas])

        x, y, j = 0, 0, 1
        while j <= veces:
            aux = []
            while x >= 0 and y >= 0 and x < filas and y < columnas:
                aux += tablero[x][y]
                x += vectorDireccion[1]
                y += vectorDireccion[2]
            if palabra in ''.join(aux):
                coincidencias[i] += 1

            aux.reverse()
            if palabra in ''.join(aux):
                coincidencias[i + 1] += 1

            x = (x + vectorDireccion[2]) % filas
            y = (y + vectorDireccion[1]) % columnas
            j += 1

    return coincidencias

# PROBADOR
sopa = [['h', 'o', 'l', 'a', 'x', 'x'],
        ['o', 'o', 'x', 'a', 'a', 'x'],
        ['l', 'x', 'l', 'x', 'l', 'x'],
        ['a', 'o', 'x', 'a', 'o', 'x'],
        ['h', 'a', 'l', 'o', 'h', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x']]

columnas = 6
filas = 6

tablero = [[0 for i in range(filas)] for j in range(columnas)]

print(buscarPalabra(sopa, 'hola', 6, 6, vectorDirecciones))

# """Pedimos cada elemento al usuario"""
# for i in range(columnas):
#     for j in range(filas):
#         print('Introduzca el elemento %d, %d: ' % (i + 1, j + 1), end='')
#         tablero[i][j] = input()
#
# print(buscarPalabra(tablero, palabra))
