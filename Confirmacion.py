"""***************************************************
--- FRANCISCO JESÚS JIMÉNEZ HIDALGO                ---
--- FUNDAMENTOS DE PROGRAMACIÓN                    ---
--- Confirmación de usuario                        ---
---************************************************"""


def esConfirmacion():
    """-> bool
    OBJ: Devuelve True si el usuario desea continurar
         False en caso contrario"""

    char = input('¿Desea continuar? S/N: ')

    if char == 'N' or char == 'n':
        continuar = False
    else:
        continuar = True

    return continuar