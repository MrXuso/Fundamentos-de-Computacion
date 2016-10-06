"""********  ORDENA NÚMEROS DE MENOR A MAYOR  ********
---    FRANCISCO JESÚS JIMÉNEZ HIDALGO J6-OCT-16   """


def menorAMayor(i, j, k):
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

    return "(" + str(i) + "," + str(j) + "," + str(k) + ")"


#Probador
print(menorAMayor(1,2,3))
print(menorAMayor(1,3,2))
print(menorAMayor(2,1,3))
print(menorAMayor(2,3,1))
print(menorAMayor(3,1,2))
print(menorAMayor(3,2,1))
