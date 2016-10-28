"""******************************************************'''
 *                     Biblioteca Dinero                  *
 *            FRANCISCO JESÚS JIMÉNEZ HIDALGO             *
'''******************************************************"""

monedasCirculacion = 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0

def dineroMonedero(monedero):
    """------------------------------------------+++
    +++tuple -> float                            +++
    ---OBJ: Dinero total en el monedero          +++
    ---PRE: monedero: tupla de enteros positivos +++
    +++------------------------------------------"""
    total = 0
    for i in range(0,len(monedasCirculacion)):
        total += monedasCirculacion[i] * monedero[i]

    return total


def enMonedasOptimas(dinero):
    """------------------------------------------+++
    +++float -> tuple                            +++
    +++OBJ: tupla con el mínimo número de monedas+++
    +++     que componen una cantidad de dinero  +++
    +++PRE: mínima subdivisión de dinero 0,01    +++
    +++------------------------------------------"""

    monedasOptimas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(monedasCirculacion)-1, -1, -1):
        if dinero / monedasCirculacion[i] >= 1:
            monedasOptimas[i] = int(dinero // monedasCirculacion[i])
            dinero = round(dinero - monedasCirculacion[i]*(dinero // monedasCirculacion[i]), 2)

    return tuple(monedasOptimas)


# PROBADOR
for dinero in monedasCirculacion:
    print(enMonedasOptimas(dinero))
