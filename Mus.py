"""---------------------------------------------+++
+++ M15-NOV-16                                  +++
+++ Francisco Jesús Jiménez Hidalgo             +++
+++ Fundamentos de programación                 +++
+++ Mus                                         +++
+++---------------------------------------------"""

"""Jugamos con dos parejas, sin señas

   Cada elemento de la baraja es un número de 2 cifras. La primera indica el
       palo 0-O 1-C 2-E 3-B. La segunda el número de la carta (siendo 0-As,
       7-Sota, 8-Caballo, 9-Rey)
"""

from random import shuffle

def inicializarBaraja():
    """ -> tuple[40 cartas barajadas]
    ---OBJ: Estrena y mezcla una baraja"""
    baraja = []
    for i in range(0, 40):
        baraja.append(i)

    shuffle(baraja)

    return baraja

def nombreSimplificadoCarta(carta):
    """ int -> str
    ---OBJ: Nombre secillo de una carta (RB, 6C, 4O, 7E...)"""
    nombre = ''

    if carta % 10 <= 6:
        nombre = str((carta % 10) + 1)
    elif carta % 10 == 7:
        nombre = 'S'
    elif carta % 10 == 8:
        nombre = 'C'
    elif carta % 10 == 9:
        nombre = 'R'

    if carta // 10 == 0:
        nombre += 'O'
    elif carta // 10 == 1:
        nombre += 'C'
    elif carta // 10 == 2:
        nombre += 'E'
    elif carta // 10 == 3:
        nombre += 'B'

    return nombre

def nombreCarta(carta):
    """ int -> str
    ---OBJ: Nombre secillo de una carta (RB, 6C, 4O, 7E...)"""
    nombre = ''

    if carta % 10 <= 6:
        nombre = str((carta % 10) + 1)
    elif carta % 10 == 7:
        nombre = 'Sota'
    elif carta % 10 == 8:
        nombre = 'Caballo'
    elif carta % 10 == 9:
        nombre = 'Rey'

    nombre += ' de '

    if carta // 10 == 0:
        nombre += 'oros'
    elif carta // 10 == 1:
        nombre += 'copas'
    elif carta // 10 == 2:
        nombre += 'espadas'
    elif carta // 10 == 3:
        nombre += 'bastos'

    return nombre


def repartirCarta(baraja):
    """ tuple [baraja] -> int cartaRepatirda, tuple [baraja restante]"""
    return baraja.pop(-1), baraja


def muestraCartas(jugador):
    """tuple
    ---OBJ: Muestra las cartas del jugador"""
    print('\t\tTus cartas son: ', end='')
    for i in range(0, 4):
        print(nombreSimplificadoCarta(jugador[i]), '', end='')
    print('')

def llevaPares(jugador):
    """tuple -> boolean
    ---OBJ: lleva alguna pareja el jugador"""


def juegoMus():
    jugador1 = []
    jugador2 = []
    jugador3 = []
    jugador4 = []
    jugadores = [jugador1, jugador2, jugador3, jugador4]
    descarte = []
    puntos = [0, 0]
    puntosGrande = [1,1,100,4,5,6,7,10,10,100]
    puntosChica = [1,1,100,94,95,96,87,98,99,100]
    puntosJuego = [1,1,3,4,5,6,7,10,10,10]

    print('¡Juguemos al mus!\n')

    '''--BARAJAMOS LAS CARTAS--'''

    baraja = inicializarBaraja()

    '''--REPARTO INICIAL'''
    # TODO: Ordenar cartas al repartirlas
    for i in range(0, 4):
        for jugador in jugadores:
            carta, baraja = repartirCarta(baraja)
            jugador.append(carta)

    '''--Nombres Jugadores--'''
    for i in range(0, 4):
        jugadores[i].append(input('Introduzca el nombre del jugador ' + str(i + 1) + ': '))

    '''--¿QUIÉN REPARTE?--'''
    print('\nReparte', jugadores[3][4], ':\n')

    '''--MOSTRAMOS LAS CARTAS A CADA JUGADOR--'''

    print(jugadores[0][4] + ' es el primero que verá sus cartas, los demás no deben mirar\n')
    for jugador in jugadores:
        print(jugador[4] + ', pulsa intro cuando estés listo para ver tus cartas:')
        input()
        muestraCartas(jugador)
        input('\nApunta tus cartas y pulsa intro cuando hayas terminado')
        print('\n' * 50)

    '''--¿ALGUIEN QUIERE MUS?--'''
    print('\nLos jugadores que NO quieran mus que contesten [N], cualquier otra cosa supondrá un Sí:\n')
    mus = True

    while mus:
        for jugador in jugadores:
            quiereMus = input('¿' + jugador[4] + ', quieres mus? S/N: ')
            if quiereMus == 'n' or quiereMus == 'N':
                mus = False
                print(jugador[4], 'ha cortado el mus')
                break

        if not mus:
            break
        print('\nTurno de descartes, los demás jugadores no deben mirar, empieza ' + jugadores[0][4] + '\n')
        for jugador in jugadores:
            print('Es tu turno, ' + jugador[4] + '. Pulsa intro para empezar')
            input()
            muestraCartas(jugador)
            print('\n¿Qué cartas te descartas? Escribe su posición [1,3,4] (sin espacios entre ellos) '
                  + 'o [N] para ninguna: ', end='')
            jugador.append(input())
            print('\n' * 50)

        '''Una vez decididos los descartes, pocedemos a repartirlas'''
        descartes = []
        for jugador in jugadores:
            descartes.append(jugador[5])

        '''Si todos descartan sus cartas, repartimos de uno en uno'''
        if (descartes[0] == descartes[1] == descartes[2] == descartes[3]) and (descartes[0] == '1,2,3,4'):
            for i in range(0,4):
                for jugador in jugadores:
                    descarte.append(jugador[i])
                    '''En caso de que no queden cartas, barajamos el descarte y lo repartimos'''
                    if len(baraja) == 0:
                        baraja = shuffle(descarte)
                        descarte = []
                    jugador[i], baraja = repartirCarta(baraja)

        '''Descartes cuando no todos descartan todas las cartas'''
        for jugador in jugadores:
            for i in range(0, len(jugador[5]), 2):
                if len(baraja) == 0:
                    baraja = shuffle(descarte)
                    descarte = []
                descarte.append(jugador[int(jugador[5][i]) - 1])
                jugador[int(jugador[5][i]) - 1], baraja = repartirCarta(baraja)

        '''Eliminamos los descartes de la tupla'''
        for jugador in jugadores:
            jugador.pop(5)

        '''Mostramos nuevamente las cartas'''
        print(jugadores[0][4] + ' es el primero que verá sus cartas, los demás no deben mirar\n')
        for jugador in jugadores:
            print(jugador[4] + ', pulsa intro cuando estés listo para ver tus cartas:')
            input()
            muestraCartas(jugador)
            input('\nApunta tus cartas y pulsa intro cuando hayas terminado')
            print('\n' * 50)

    '''--JUGAMOS A GRANDES Y A CHICAS--'''
    puntosEnvite = [0,0]
    for j in range(0,2):
        if j == 0:
            print('\n\n¡Turno de jugar a Grandes!\n')
        elif j ==1:
            print('\n\n¡Turno de jugar a Chicas!\n')
        puntosEnvite[j] = False
        for i in range(0, 4):
            jugador = jugadores[i]
            accion = input('\nTurno de ' + jugador[4] + '. ¿[P]asas o [E]nvidas?: ')
            if accion == 'E' or accion == 'e':
                accion = int(input('¿Cuántas envidas?: '))
                puntosEnvite[j] = accion

                accion = input(
                    jugadores[(i+1) % 4][4] + ', ' + jugadores[(i+3) % 4][4] + ', ¿[P]asáis, lo [V]éis o [S]ubís?: ')
                if accion == 'P' or accion == 'p':
                    puntosEnvite[j] = 1
                    puntos[i % 2] += 1
                elif accion == 'S' or accion == 's':
                    cantidad = int(input('¿Cuántas subís?: '))
                    puntosEnvite[j] += cantidad

                break

        if puntosEnvite[j] and puntosEnvite[j] != 1:
            accion = 'S'
            while accion == 'S' or accion == 's':
                i = (i+1)%4
                accion = input(
                    jugadores[(i + 1) % 4][4] + ', ' + jugadores[(i + 3) % 4][4] + ', ¿[P]asáis, lo [V]éis o [S]ubís?: ')
                if accion == 'P' or accion == 'p':
                    puntos[i % 2] += puntosEnvite[j]
                    break
                elif accion == 'S' or accion == 's':
                    cantidad = int(input('¿Cuántas subís?: '))
                    puntosEnvite[j] += cantidad
                elif accion == 'V' or accion == 'v':
                    break

    '''--JUGAMOS A PARES--'''
    for jugador in jugadores:


    '''--JUGAMOS A JUEGO O PUNTO--'''
    # TODO: Quién tiene juego?
        # TODO: Si alguien tiene juego, juego

        # TODO: Si Nadie tiene juego, punto

juegoMus()