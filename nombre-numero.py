"""******************************************************'''
 *                NOMBRE DE UN NÚMERO DADO                *
 *            FRANCISCO JESÚS JIMÉNEZ HIDALGO             *
'''******************************************************"""

def nombreNumero(n):
    """int -> str                              '''
     * OBJ: nombre de un número dado           '''
     * PRE: 30 <= n < 99                       """

    if n//10 == 3:
        numero = 'treinta'
    elif n//10 == 4:
        numero = 'cuarenta'
    elif n // 10 == 5:
        numero = 'cincuenta'
    elif n // 10 == 6:
        numero = 'sesenta'
    elif n // 10 == 7:
        numero = 'setenta'
    elif n // 10 == 8:
        numero = 'ochenta'
    elif n // 10 == 9:
        numero = 'noventa'

    if n % 10 != 0:
        numero += ' y '

    if n % 10 == 1:
        numero += 'uno'
    elif n % 10 == 2:
        numero += 'dos'
    elif n % 10 == 3:
        numero += 'tres'
    elif n % 10 == 4:
        numero += 'cuatro'
    elif n % 10 == 5:
        numero += 'cinco'
    elif n % 10 == 6:
        numero += 'seis'
    elif n % 10 == 7:
        numero += 'siete'
    elif n % 10 == 8:
        numero += 'ocho'
    elif n % 10 == 9:
        numero += 'nueve'

    return numero