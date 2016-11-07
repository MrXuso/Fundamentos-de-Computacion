"""***************************************************
--- FRANCISCO JESÚS JIMÉNEZ HIDALGO                ---
--- FUNDAMENTOS DE PROGRAMACIÓN                    ---
--- Sopa de letras                                 ---
---************************************************"""

palabra = input('Introduzca la palabra a buscar: ')
filas = int(input('Introduzca el número de filas: '))
columnas = int(input('Introduzca el número de columnas: '))

tablero = [[0 for i in range(filas)] for j in range(columnas)]

"""Pedimos cada elemento al usuario"""
for i in range(columnas):
    for j in range(filas):
        print('Introduzca el elemento %d, %d: ' %(i+1, j+1), end='')
        tablero[i][j] = input()


def buscarPalabra(tablero, palabra):
    """list[][], str -> str
    +++OBJ: busca la palabra en la sopa de letras
    +++PRE: tablero lista de string"""
    aux = []
    coincidencias = 0

    for i in range(filas):
        aux.clear()
        for j in range(columnas):
            aux += tablero[i][j]
        if palabra in ''.join(aux):
            coincidencias += 1

    print('Se han encontrado %d %s en sentido E' %(coincidencias,palabra))

    coincidencias = 0
    for i in range(filas-1, -1, -1):
        aux.clear()
        for j in range(columnas-1, -1, -1):
            aux += tablero[j][i]
        if palabra in ''.join(aux):
            coincidencias += 1

    print('Se han encontrado %d %s en sentido S' %(coincidencias,palabra))

    coincidencias = 0
    for i in range(columnas):
        aux.clear()
        for j in range(filas):
            aux += tablero[j][i]
        if palabra in ''.join(aux):
            coincidencias += 1

    print('Se han encontrado %d %s en sentido N' %(coincidencias,palabra))

    coincidencias = 0
    for i in range(columnas-1, -1, -1):
        aux.clear()
        for j in range(filas-1, -1, -1):
            aux += tablero[i][j]
        if palabra in ''.join(aux):
            coincidencias += 1

    print('Se han encontrado %d %s en sentido O' %(coincidencias,palabra))
buscarPalabra(tablero, palabra)

# PROBADOR
for i in range(columnas):
    for j in range(filas):
        print('%3s' % tablero[i][j], end='')
    print('')