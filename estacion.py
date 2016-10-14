"""******************************************************'''
 *                    ESTACIÓN DEL MES                    *
 *            FRANCISCO JESÚS JIMÉNEZ HIDALGO             *
'''******************************************************"""


def estacion(dia, mes):
    """int, int -> str                              '''
     * OBJ: estación del año dado un día y un mes   '''
     * PRE: día y mes fecha válidas                 """
    mmdd = mes * 100 + dia

    if mmdd <= 309:
        estacion = 'invierno'
    elif mmdd <= 620:
        estación = 'primavera'
    elif mmdd <= 922:
        estacion = 'verano'
    elif mmdd <= 1220:
        estacion = 'otoño'
    else:
        estacion = 'invierno'

    return estacion

dia = int(input('Intoduzca un día: '))
mes = int(input('Intoduzca un mes: '))
print(estacion(dia, mes))