"""******************************************************'''
 *                       PECL1 2016                       *
 *            FRANCISCO JESÚS JIMÉNEZ HIDALGO             *
'''******************************************************"""

from calendar import monthrange


def nombreMes(mes):
    """int -> str             ---
    ---OBJ: nombre del mes n  ---
    ---PRE 1 <= mes <= 12     """
    if mes == 1:
        mes = 'enero'
    elif mes == 2:
        mes = 'febrero'
    elif mes == 3:
        mes = 'marzo'
    elif mes == 4:
        mes = 'abril'
    elif mes == 5:
        mes = 'mayo'
    elif mes == 6:
        mes = 'junio'
    elif mes == 7:
        mes = 'julio'
    elif mes == 8:
        mes = 'agosto'
    elif mes == 9:
        mes = 'septiembre'
    elif mes == 10:
        mes = 'octubre'
    elif mes == 11:
        mes = 'noviembre'
    elif mes == 12:
        mes = 'diciembre'
    else:
        mes = 'No has introducido el número de un mes'

    return mes


def cuatroPrimerasSemanas(mes, anio):
    """int, int -> str                                  ---
    ---OBJ: Imprime las cuatro primeras semanas con     ---
    ---     formato de un mes de un año dado            ---
    ---PRE: 1 <= mes <= 12, anio > 1582                 """
    diaInicial = monthrange(anio,mes)[0]
    diasEnElMes = monthrange(anio,mes)[1]

    # Nombre del mes y año
    print('\n\t\t' + nombreMes(mes), anio)
    #Días de la semana
    print('     LU  MA  MI  JU  VI  SA  DO')

    # Primera semana
    print('    ' * (diaInicial), end='   ')

    # Semana 1-4
    for dia in range(1, 24):
        # Si es domingo, retorno de carro
        if (dia + diaInicial - 1) % 7 == 0:
            print('\n   ', end='')
        # Imprimimos en pantalla el número
        print('%4d' % dia, end='')

    print('\n')

print('***LIBRERÍA CALENDARIO***')
try:
    mes = int(input('Introduzca el número de un mes: '))
except ValueError:
    print('El mes debe de ser un entero entre 1 y 12')
    exit()
try:
    anio = int(input('Introduzca un año: '))
except ValueError:
    print('El año debe ser un entero mayor que 1582')
    exit()

if 1 < mes > 12:
    print('El mes debe de ser un entero entre 1 y 12')
else:
    if anio < 1582:
        print('El año debe ser un entero mayor que 1582')
    else:
        cuatroPrimerasSemanas(mes, anio)
