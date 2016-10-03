'''********** CALCULA SI UN AÑO ES BISIESTO *********'''

def esBisiesto(anio):
    """int -> boolean
    OBJ: Es el año bieisto?
    PRE: anio >= 1582"""
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0

print(esBisiesto(2016))     # True, 2016 es bisiesto (múltiplo de 4)
print(esBisiesto(2015))     # False, 2015 no es bisiesto
print(esBisiesto(2100))     # False, 2100 no es bisiesto (múltiplo de 100)
print(esBisiesto(2000))     # True, 2000 es bisiesto (múltiplo de 400)
