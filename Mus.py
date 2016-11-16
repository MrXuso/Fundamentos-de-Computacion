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
    print('\t\tTus cartas son: ', end='')
    for i in range(0, 4):
        print(nombreSimplificadoCarta(jugador[i]), '', end='')
    print('')

def juegoMus():
    jugador1 = []
    jugador2 = []
    jugador3 = []
    jugador4 = []
    jugadores = [jugador1, jugador2, jugador3, jugador4]
    descarte = []

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
        input('\nPiensa si vas a querer mus y pulsa intro cuando hayas terminado')
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
        # TODO: Descartes normales
            # TODO: Barajas sin cartas

        '''Eliminamos los descartes de la tupla'''
        for jugador in jugadores:
            jugador.pop(5)

        '''Mostramos nuevamente las cartas'''
        print(jugadores[0][4] + ' es el primero que verá sus cartas, los demás no deben mirar\n')
        for jugador in jugadores:
            print(jugador[4] + ', pulsa intro cuando estés listo para ver tus cartas:')
            input()
            muestraCartas(jugador)
            input('\nPiensa si vuelves a querer mus y pulsa intro cuando hayas terminado')
            print('\n' * 50)

    '''--JUGAMOS A GRANDES--'''
    # TODO: Grandes

    '''--JUGAMOS A CHICAS--'''
    # TODO: Chicas

    '''--JUGAMOS A PARES--'''
    # TODO: Quién tiene pares?
        # TODO: Pares

    '''--JUGAMOS A JUEGO O PUNTO--'''
    # TODO: Quién tiene juego?
        # TODO: Si alguien tiene juego, juego

        # TODO: Si Nadie tiene juego, punto

juegoMus()