"""***************************************************
--- FRANCISCO JESÚS JIMÉNEZ HIDALGO                ---
--- FUNDAMENTOS DE PROGRAMACIÓN                    ---
--- Fechas                                         ---
---************************************************"""

from calendar import monthrange
from bisiesto import esBisiesto
from NombreMes import nombreMes

DIAS_MES = [31,29,31,30,31,30,31,31,30,31,30,31]


def fechaValida(anio, mes, dia):
    """str -> boolean
    ---OBJ: Es la fecha correcta"""

    esCorrecto = True

    if mes < 1 or mes > 12:
        esCorrecto = False

    '''monthrange(anio, mes) devuelve el último día del mes de ese año'''
    if dia < 1 or dia > DIAS_MES[mes - 1]:
        esCorrecto = False

    if mes == 2 and dia == 29:
        if not esBisiesto(anio):
            esCorrecto = False

    return esCorrecto

def formatoFecha(dia, mes, anio):
    """--------------------------------------------------+++
    +++int, int, int                                     +++
    +++OBJ: Imprime la fecha como dd/mm/aaaa             +++
    +++PRE: dia, mes y anio fecha correcta               +++
    +++--------------------------------------------------"""
    if dia < 10:
        dia = '0' + str(dia)
    else:
        dia = str(dia)

    if mes < 10:
        mes = '0' + str(mes)
    else:
        mes = str(mes)

    if anio < 10:
        anio = '000' + str(anio)
    elif anio < 100:
        anio = '00' + str(anio)
    elif anio < 1000:
        anio = '0' + str(anio)
    else:
        anio = str(anio)

    print(dia, '/', mes, '/', anio, end='', sep='')


def nombreNumero(numero):
    """int -> str
    ---OBJ: nombre de numero mayor que 0"""

    DEFINIDOS = ['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'siete', 'Ocho', 'Nueve', 'Diez'
        , 'Once', 'Doce', 'Trece', 'Catorce', 'Quince']

    UNIDADES = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']

    DECENAS = ['', 'Dicei', 'Veinti', 'Treinta y ']

    if numero < 15:
        nombre = DEFINIDOS[numero-1]
    elif numero == 20:
        nombre = 'veinte'
    elif numero == 30:
        nombre = 'treinta'
    else:
        nombre = DECENAS[numero//10] + UNIDADES[numero % 10 - 1]

    return nombre


anio, mes, dia = 0, 0, 0
while not fechaValida(anio, mes, dia):
    print('')
    try:
        anio = int(input('Introduzca el año: '))
        mes = int(input('Introduzca el mes: '))
        dia = int(input('Introduzca el día: '))
    except ValueError:
        print('Fecha incorrecta')

    if not fechaValida(anio, mes, dia):
        print('Fecha incorrecta')


formatoFecha(dia, mes, anio)
print('\n' + nombreNumero(dia) + ' de ' + nombreMes(mes) + ' de', anio)