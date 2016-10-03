'''********** CALCULA SI UN AÑO ES BISIESTO *********'''

def esBisiesto(anio):
    """int -> boolean
    OBJ: Es el año bieisto?
    PRE: anio >= 1582"""
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0

print(esBisiesto(2200))