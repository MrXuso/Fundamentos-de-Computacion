"""***************************************************
--- FRANCISCO JESÚS JIMÉNEZ HIDALGO                ---
--- FUNDAMENTOS DE PROGRAMACIÓN                    ---
--- Elemento Lista                                 ---
---************************************************"""


def posicionLista(elementoBuscado, lista):
    """ int, list -> boolean/int
    ---OBJ: Posición en la lista de un elemento"""

    posicion = False
    for i in range(len(lista)):
        if elementoBuscado == lista[i]:
            posicion = i + 1
            break

    return posicion

print(posicionLista(4,[1,2,3,4,5,6,7]))
