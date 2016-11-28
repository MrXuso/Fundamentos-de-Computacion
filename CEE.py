"""***************************************************
--- FRANCISCO JESÚS JIMÉNEZ HIDALGO                ---
--- FUNDAMENTOS DE PROGRAMACIÓN                    ---
--- CEE                                            ---
---************************************************"""

from collections import namedtuple

NOMBRES_PAISES = ('Alemania', 'Francia', 'Reino Unido', 'Italia', 'España')
tPais = namedtuple('Pais', 'nombre, rentaPerCapita, poblacion')
ESTADISTICA_PAISES = (tPais('Alemania', 30100, 82605000)
                      , tPais('Francia', 28800, 64770000)
                      , tPais('Reino Unido', 27600, 65893000)
                      , tPais('Italia', 26200, 60721000)
                      , tPais('España', 26500, 46427000))


def nombrePaises(paises):
    """tuple (pais1, ..., paisN)
    ---OBJ: Nombre de los paises"""
    for pais in paises:
        print(pais)


def nombrePais(paises, n):
    """tuple (pais1, ..., paisN), int -> str
    ---OBJ: Nombre pais posicion n
    ---PRE: n <= numero de paises"""
    return paises[n - 1]


def estaPais(paises, pais):
    """tuple (pais1, ..., paisN), str -> boolean
    ---OBJ: Está el pais entre los países dados?"""

    return pais in paises


def paisesConMasHabitantes(paises, poblacion):
    """tuple (tPais1, ..., tPaisN), int -> int
    ---OBJ: total de países con más habitantes que el argumento dado"""

    cuenta = 0

    for pais in paises:
        if pais.poblacion > poblacion:
            cuenta += 1

    return cuenta


def poblacionAcumulada(paises):
    """tuple (tPais1, ..., tPaisN) -> int
    ---OBJ: población acumulada de los pasíses dados"""

    cuenta = 0

    for pais in paises:
        cuenta += pais.poblacion

    return cuenta


def tablaPaises(nombresPaises, paises):
    """tuple(nombresPaises), tuple (tPais1, ..., tPaisN)
    ---OBJ: Construye una tabla con los países y sus datos"""

    print('\n', '%15s' % 'País', '  |  Renta  |  ',
          'Población |  %Poblacion', sep='', )
    print('   _____________________________________________________')

    for i in range(0, len(nombresPaises)):

        porcentajePoblacion = round(paises[i].poblacion * 100 / poblacionAcumulada(paises), 5)

        print('\n', '%15s'%nombresPaises[i], '  |  ', '%5d' % paises[i].rentaPerCapita, '  |  '
              , '%8d' % paises[i].poblacion, '  |  ', '%d' % porcentajePoblacion, '%', sep='',)


def rentaMedia(paises):
    """tuple (tPais1, ..., tPaisN) -> int
    ---OBJ: renta media entre todos los países"""

    renta = 0

    for pais in paises:
        renta += (pais.rentaPerCapita * pais.poblacion)/poblacionAcumulada(ESTADISTICA_PAISES)

    return int(renta)


def hayPaisConMenosPoblacion(paises, poblacion):
    """tuple (tPais1, ..., tPaisN), int -> boolean
    ---OBJ: Hay algún país con menos habitantes que el argumento?"""

    i = 0
    hayPais = False

    while i < len(paises):
        if paises[i].poblacion < poblacion:
            hayPais = True
            break

        i += 1

    return hayPais


def aniadirPaises():
    pais = ''
    nombresPaises = []
    rentas = []
    poblaciones = []
    estadisticasPaises = []

    while pais != 'fin':
        pais = input('\nIntroduzca el nombre del país (FIN para terminar): ')

        if pais == 'fin' or pais == 'FIN':
            break
        else:
            try:
                renta = int(input('Introduzca la renta per cápita del pais: '))
                poblacion= int(input('Introduzca la poblacion del pais: '))
            except ValueError:
                print('Los datos introducidos deben ser números enteros')
                pais = ''
                continue

        nombresPaises.append(pais)
        rentas.append(renta)
        poblaciones.append(poblacion)

        for i in range(0, len(nombresPaises)):
            estadisticasPaises.append(tPais(nombresPaises[i], rentas[i], poblaciones[i]))

    return estadisticasPaises, nombresPaises

'''Bloque ejecutivo'''
print('\n\t\t\tESTADÍSTICAS CEE\n\n')
aux = aniadirPaises()
estadisticasPaises, nombresPaises = aux[0], aux[1]
print('')
nombrePaises(nombresPaises)
print('')
print(nombrePais(nombresPaises,1))
print('')
print(estaPais(nombresPaises, 'España'))
print('')

"""
# PROBADOR
print('')
nombrePaises(NOMBRES_PAISES)
print('')
print(nombrePais(NOMBRES_PAISES, 1))
print('')
print(estaPais(NOMBRES_PAISES, 'España'))
print(estaPais(NOMBRES_PAISES, 'Austria'))
print('')
print(paisesConMasHabitantes(ESTADISTICA_PAISES, 63000000))
print('')
print(poblacionAcumulada(ESTADISTICA_PAISES))
print('')
tablaPaises(NOMBRES_PAISES, ESTADISTICA_PAISES)
print('')
print(rentaMedia(ESTADISTICA_PAISES))
print('')
print(hayPaisConMenosPoblacion(ESTADISTICA_PAISES, 10000))
print(hayPaisConMenosPoblacion(ESTADISTICA_PAISES, 100000000000))
print('')
print(aniadirPaises())
"""
