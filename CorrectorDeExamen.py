"""******************************************************'''
 *                  Corrector de examen                   *
 *            FRANCISCO JESÚS JIMÉNEZ HIDALGO             *
 *           Fdtos de programación L7-NOV-2016            *
'''******************************************************"""


def correctorDeExamen(examenesAlumnos, correcion, criterios):
    """tuple de tupples, tuple, tuple -> tuple de tuples
    ---OBJ: Notas de los exámenes de los alumnos
    ---PRE: examenesAlumnos [[str nombre, resp1, resp2...][str nombre. resp1...]]
    ---     correccion [respCorr1, respCorr2, ...]
    ---     criterios [correcta, incorrecta, blanco]"""

    for i in range(0, len(examenesAlumnos)):
        nota = 0
        preguntas = [0,0,0]
        for j in range(1, len(examenesAlumnos[i])):
            if examenesAlumnos[i][j] == correcion[j-1]:
                nota += criterios[0]
                preguntas[0] += 1
            elif examenesAlumnos[i][j] == '':
                nota += criterios[2]
                preguntas[2] += 1
            elif examenesAlumnos != correcion[j-1]:
                nota += criterios[1]
                preguntas[1] += 1

        examenesAlumnos[i].append(nota)
        examenesAlumnos[i].append(preguntas)

    return examenesAlumnos

examenes = [['Jesús', 'a', 'b', 'a'],['David', 'c', 'b', 'a'],['Sara', 'c', 'c', 'c']]
correccion = ['a','b','a']
criterios = [3,0,0]
corregidos = correctorDeExamen(examenes, correccion, criterios)

for i in range(0,3):

    print(corregidos[i][0], 'ha obtenido', corregidos[i][-2], 'puntos,', '%.2f' %((corregidos[i][-1][0] / (len(correccion)*criterios[0]))*100) , '% de aciertos')