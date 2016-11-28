"""***************************************************
--- FRANCISCO JESÚS JIMÉNEZ HIDALGO                ---
--- FUNDAMENTOS DE PROGRAMACIÓN                    ---
--- Tic Tac Toe                                    ---
---************************************************"""
from random import randint


def ticTacToe():
    """OBJ: Juega al tic tac toe"""
    terminado = False

    '''Rejilla que llenamos con las X y O'''
    rejilla = [[' ', '|', ' ', '|', ' '],
               ['-', '-', '-', '-', '-'],
               [' ', '|', ' ', '|', ' '],
               ['-', '-', '-', '-', '-'],
               [' ', '|', ' ', '|', ' ']]

    while not terminado:

        """Controlamos que la posición esté vacía"""
        correcto = False
        while not correcto:
            posicion = input('\nIntroduzca las coordenadas de su ficha:')
            posicion = [(int(posicion[0])-1)*2, (int(posicion[2])-1)*2]
            if estaVacia(rejilla, posicion):
                correcto = True
                rejilla[(posicion[0])][(posicion[1])] = 'X'

        if haGanado(rejilla):
            print('')
            imprimirRejilla(rejilla)
            print('\n¡Enhorabuena!, has ganado')
            break

        correcto = False
        while not correcto:
            posicionX = (randint(1, 3) - 1) * 2
            posicionY = (randint(1, 3) - 1) * 2
            if estaVacia(rejilla, [posicionY, posicionX]):
                correcto = True
                rejilla[posicionY][posicionX] = 'O'

        print('')
        imprimirRejilla(rejilla)

        if haGanado(rejilla):
            print('\nVaya... Has perdido')
            break

def estaVacia(rejilla, posicion):
    vacia = True
    if rejilla[posicion[0]][posicion[1]] != ' ':
        vacia = False

    return vacia

def haGanado(rejilla):
    ganado = False
    for i in range(1,4):
        if rejilla[(i-1)*2][0] == rejilla[(i-1)*2][2] == rejilla[(i-1)*2][4] != ' ':
            ganado = True

    for j in range(1,4):
        if rejilla[0][(j-1)*2] == rejilla[2][(j-1)*2] == rejilla[4][(j-1)*2] != ' ':
            ganado = True

    if rejilla[0][0] == rejilla[2][2] == rejilla[4][4] != ' ':
        ganado = True

    if rejilla[0][4] == rejilla[2][2] == rejilla[4][0] != ' ':
        ganado = True

    return ganado

def imprimirRejilla(rejilla):
    for i in range(0,5):
        print('')
        for j in range(0,5):
            print(rejilla[i][j], end='')
    print('')

from Confirmacion import esConfirmacion

ticTacToe()
while esConfirmacion():
    ticTacToe()