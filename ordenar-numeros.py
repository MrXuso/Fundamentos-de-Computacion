"""********  ORDENA NÚMEROS DE MENOR A MAYOR  ********
---    FRANCISCO JESÚS JIMÉNEZ HIDALGO J6-OCT-16   """


def menorAMayor(i, j, k):
    """num, num, num -> num, num, num
        OBJ: ordena de menor a mayor
        PRE: no hay"""
    if i <= j:
        if j < k:
            ordenados = i, j, k
        else:
            if i < k:
                ordenados = i, k, j
            else:
                ordenados = k, i, j
    else:
        if k <= j:
            ordenados = k, j, i
        else:
            if k <= i:
                ordenados = j, k, i
            else:
                ordenados = j, i, k

    return ordenados


def menorAMayorCambio(i, j, k):
    """int, int, int
    OBJ: ordena de menor a mayor
    PRE: no hay"""

    if i > j:
        aux = i
        i = j
        j = aux

    if j > k:
        aux = j
        j = k
        k = aux

        if i > j:
            aux = i
            i = j
            j = aux

    return i,j,k


# Probador
print(menorAMayorCambio(1,2,3))
print(menorAMayorCambio(1,3,2))
print(menorAMayorCambio(2,1,3))
print(menorAMayorCambio(2,3,1))
print(menorAMayorCambio(3,1,2))
print(menorAMayorCambio(3,2,1))
