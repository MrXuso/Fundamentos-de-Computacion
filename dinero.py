"""******************************************************'''
 *                     Biblioteca Dinero                  *
 *            FRANCISCO JESÚS JIMÉNEZ HIDALGO             *
'''******************************************************"""

monedasCirculacion = 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500

def dineroMonedero(monedero):
    """tuple -> float
    OBJ: Dinero total en el monedero"""
    total = 0
    for i in range(0,len(monedasCirculacion)):
        total += monedasCirculacion[i] * monedero[i]

    return total

print(dineroMonedero((0,0,0,0,0,0,0,0,0,0,0,0,0,0,1)))