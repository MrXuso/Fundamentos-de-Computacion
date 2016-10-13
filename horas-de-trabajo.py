"""*************  HORAS TRABAJADAS  *************---
--- FRANCISCO JESÚS JIMÉNEZ HIDALGO J12-OCT-2016 """


def enMinutos(hora):
    """str -> int
    OBJ: 'HH:MM' a minutos
    PRE: formato 'horas:minutos',
        estando codificadas las horas en 24h"""

    hora = hora.split(':')

    return int(hora[0]) * 60 + int(hora[1])


def enHorasMinutos(minutos):
    """int -> str
    OBJ: minutos a 'horas:minutos'
    PRE: minutos >= 0"""

    horas = str(minutos//60)

    minutos %= 60

    '''Convertimos a formato HH:MM'''
    if minutos == 0:
        minutos = '00'
    elif minutos < 10:
        minutos = '0' + str(minutos)
    else:
        minutos = str(minutos)

    return horas + ':' + minutos


def tiempoTrabajado(horaEntrada, horaSalida):
    """str, str -> int, boolean
        OBJ: Dada la hora de entrada y de salida del trabajo, devuelve cuánto ha trabajado
            y una alerta si son más de 8 horas
        PRE: las horas vienen codificadas como 'horas:minutos' en formato 24h"""

    entrada = enMinutos(horaEntrada)
    salida = enMinutos(horaSalida)

    if entrada < salida:                                # Entra y sale de trabajar el mismo día
        trabajado = salida - entrada
    else:                                               # Entra a trabajar dos días consecutivos
        trabajado = (24 * 60) - entrada + salida

    masDeOchoHoras = False
    if trabajado > 8 * 60:                              # Si ha trabajado más de 8 horas
        masDeOchoHoras = True

    return enHorasMinutos(trabajado), masDeOchoHoras

"""
#PROBADOR
print(tiempoTrabajado('11:00','11:15'))
print(tiempoTrabajado('12:33','20:33'))
print(tiempoTrabajado('12:30','14:15'))
print(tiempoTrabajado('23:00','2:13'))
print(tiempoTrabajado('23:55','2:15'))
print(tiempoTrabajado('6:15','19:30'))
"""

print('\nHORAS TRABAJADAS\n----------------\n')
print('Introduce la hora de entrada (HH:MM): ', end='')
horaEntrada = input()
print('Introduce la hora de salida (HH:MM): ', end='')
horaSalida = input()

print('Ha trabajado', tiempoTrabajado(horaEntrada, horaSalida)[0])
if tiempoTrabajado(horaEntrada, horaSalida)[1]:
    print('ALERTA')