"""***********  NOMBRE DEL MES  ************
-- J6.OCT-16                             """

def nombreMes(numeroMes):
    """int -> str
    OBJ: Nombre del mes
    PRE  12 >= mes >= 1 """
    if numeroMes == 1:
        mes = 'Enero'
    elif numeroMes == 2:
        mes = 'Febrero'
    elif numeroMes == 3:
        mes = 'Marzo'
    elif numeroMes == 4:
        mes = 'Abril'
    elif numeroMes == 5:
        mes = 'Mayo'
    elif numeroMes == 6:
        mes = 'Junio'
    elif numeroMes == 7:
        mes = 'Julio'
    elif numeroMes == 8:
        mes = 'Agosto'
    elif numeroMes == 9:
        mes = 'Septiembre'
    elif numeroMes == 10:
        mes = 'Octubre'
    elif numeroMes == 11:
        mes = 'Noviembre'
    elif numeroMes == 12:
        mes = 'Diciembre'

    return mes

print(nombreMes(8))

