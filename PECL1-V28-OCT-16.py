"""***************************************************
--- FRANCISCO JESÚS JIMÉNEZ HIDALGO                ---
--- FUNDAMENTOS DE PROGRAMACIÓN                    ---
--- PECL1 V28-OCT-16                               ---
---************************************************"""
from calendar import monthrange


def diaDeLaSemana (dia, mes, anio):
    """-------------------------------------------------+++
    +++int, int, int -> int                             +++
    +++OBJ: Día de la semana que es un día de una fecha +++
    +++     concreta (Lunes = 0, Domingo = 6)           +++
    +++PRE: dia, mes y anio fecha correcta              +++
    +++-------------------------------------------------"""
    diaInicial = monthrange(anio, mes)[0]

    return (dia + diaInicial - 1) % 7


def calendarioJuliano(dia, mes, anio):
        """--------------------------------------------------+++
        +++int, int, int -> int                              +++
        +++OBJ: Calendario Gregoriano a Juliano              +++
        +++PRE: dia, mes y anio fecha correcta y anio >= -44 +++
        +++--------------------------------------------------"""
        fechaJuliana = 0

        for indiceMes in range (1, mes):
            fechaJuliana += monthrange(1, indiceMes)[1]

        fechaJuliana += dia

        '''Si es bisiesto, el día debe de ser después del 2 de febrero'''
        if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
            if mes > 2:
                fechaJuliana += 1
            elif mes == 2 and dia > 28:
                fechaJuliana += 1

        return fechaJuliana


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


print('*** CALENDARIO JULIANO ***\n')

'''Pedimos al usuario los datos y comprobamos que son enteros'''
try:
    dia = int(input('Introduce un día: '))
except ValueError:
    print('El día debe ser un entero entre 1 y 31')
    exit()

try:
    mes = int(input('Introduce un mes: '))
except ValueError:
    print('El mes debe ser un entero entre 1 y 12')
    exit()

try:
    anio = int(input('Introduce un año: '))
except ValueError:
    print('El año debe de ser un entero')
    exit()

print('')

'''Si el usuario ha introducido una fecha incorrecta, le avisamos
   , en caso contrario, mostramos el resultado'''
if dia < 1 or dia > monthrange(anio, mes)[1]:
    print('El mes %d de %d no tiene día %d' %(mes, anio, dia))
elif dia == 29 and not((anio % 4 == 0 and anio % 100 != 100) or anio % 400 == 0):
    print('El mes %d de %d no tiene día %d' % (mes, anio, dia))
elif mes < 1 or mes > 12:
    print('El calendario gregoriano no tiene el mes %d de %d' % (mes, anio))
else:
    print('El ', end='')
    formatoFecha(dia, mes, anio)
    print(' es el ', calendarioJuliano(dia, mes, anio)
          , ' del calendario juliano y es el ', diaDeLaSemana(dia, mes, anio)
          , ' de la semana', sep='')


'''
# PROBADOR diaDeLaSemana()
print(diaDeLaSemana(28,10,2016))         # Viernes, día del examen
print(diaDeLaSemana(1,11,2016))          # Martes de la semana que viene
print(diaDeLaSemana(4,2,1996))           # Domingo, día que nací (sé el día de la semana que nací)

# PROBADOR calendarioJuliano()
print(calendarioJuliano(1,1,-44))       # 1, primer día del calendario funciona
print(calendarioJuliano(14,10,2016))    # 288, citado en el examen

#PROBADOR formatoFecha()
formatoFecha(1,1,1)                     # 01/01/0001
print('')
formatoFecha(22,10,22)                  # 22/10/0022
print('')
formatoFecha(31,11,333)                 # 31/11/0333
print('')
formatoFecha(4,9,4444)                  # 04/09/4444
'''