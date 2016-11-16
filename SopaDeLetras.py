"""***************************************************
--- FRANCISCO JESÚS JIMÉNEZ HIDALGO                ---
--- FUNDAMENTOS DE PROGRAMACIÓN                    ---
--- Sopa de letras                                 ---
---************************************************"""

vectorDirecciones = [['E', 0, 1], ['O'], ['S', 1, 0], ['N'],
                     ['SE', 1, 1], ['NO'], ['SO', -1, 1], ['NE']]


def buscarPalabra(tablero, palabra, filas, columnas, vectorDirecciones):
    """list[][], str -> list [coincidencias E, O, S, N, SE, NO, SO, NE
    +++OBJ: busca la palabra en la sopa de letras
    +++PRE: tablero lista de string"""
    coincidencias = [0 for i in range(8)]

    """Horizontal/Vertical"""
    for i in range(0, 4, 2):
        vectorDireccion = vectorDirecciones[i]

        """Veces que tenemos que buscar una palabra en una matriz filas x columnas"""
        veces = max(filas, columnas)

        x, y, j = 0, 0, 1
        while j <= veces:
            aux = []
            while x >= 0 and y >= 0 and y < filas and x < columnas:
                aux += tablero[y][x]
                y += vectorDireccion[1]
                x += vectorDireccion[2]

            if palabra in ''.join(aux):
                coincidencias[i] += 1
            aux.reverse()
            if palabra in ''.join(aux):
                coincidencias[i + 1] += 1

            y = (y + vectorDireccion[2]) % filas
            x = (x + vectorDireccion[1]) % columnas
            j += 1

    """DIAGONALES"""
    for i in range(4, 8, 2):
        vectorDireccion = vectorDirecciones[i]
        for j in range(0, filas):

            if j == 0:
                if i == 4:
                    delInicio = columnas-1
                    delFinal = -1
                    incremento = -1
                elif i == 6:
                    delInicio = 0
                    delFinal = columnas
                    incremento = 1
            else:
                if i == 4:
                    delInicio = 0
                    delFinal = 1
                    incremento = 1
                if i == 6:
                    delInicio = columnas-1
                    delFinal = columnas
                    incremento = 1

            for k in range(delInicio, delFinal, incremento):
                y, x = j, k
                aux = []
                while x >= 0 and y >= 0 and y < filas and x < columnas:
                    aux += tablero[y][x]
                    x += vectorDireccion[1]
                    y += vectorDireccion[2]

                if palabra in ''.join(aux):
                    coincidencias[i] += 1
                aux.reverse()
                if palabra in ''.join(aux):
                    coincidencias[i + 1] += 1

    return coincidencias

"""
# PROBADOR
sopa = [['h', 'o', 'l', 'a', 'x', 'x', 'a', 'l', 'o', 'h'],
        ['x', 'o', 'i', 'n', 'f', 'o', 'z', 'x', 'o', 'x'],
        ['x', 'x', 'l', 'm', 'o', 'l', 'a', 'l', 'x', 'x'],
        ['x', 'x', 'x', 'a', 'x', 'x', 'a', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'a', 'x', 'x', 'x', 'x', 'x'],
        ['h', 'x', 'x', 'l', 'x', 'x', 'a', 'x', 'x', 'a'],
        ['o', 'x', 'o', 'x', 'x', 'x', 'x', 'l', 'x', 'l'],
        ['l', 'h', 'x', 'x', 'x', 'x', 'x', 'x', 'o', 'o'],
        ['a', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'h']]


print(buscarPalabra(sopa, 'hola', 10, 10, vectorDirecciones))
"""
palabra = input('Introduzca la palabra a buscar: ')
filas = int(input('Introduzca el número de filas: '))
columnas = int(input('Introduzca el número de columnas: '))
tablero = [[0 for i in range(filas)] for j in range(columnas)]

"""Pedimos cada elemento al usuario"""
for i in range(columnas):
    for j in range(filas):
        print('Introduzca el elemento %d, %d: ' % (i + 1, j + 1), end='')
        tablero[i][j] = input()

coincidencias = buscarPalabra(tablero, palabra, filas, columnas, vectorDirecciones)

print('\n\n\nHas introducido la siguiente sopa:\n')

for i in range(0, filas):
    for j in range(0, columnas):
        print('%3s' %tablero[i][j], end='')
    print('')
print('')

for i in range(0,8):
    print('Se han encontrado', coincidencias[i], 'en sentido', vectorDirecciones[i][0])
