'''*********  CALCULA EL PERÍMETRO Y EL ÁREA DE UNA CIRCUNFERENCIA DADO EL RADIO  ********'''

from math import pi  # importamos π desde la biblioteca math


def perimetro(radio):
    """float -> float
    OBJ: Perímetro dado el radio
    PRE: radio >= 0"""
    return 2 * radio * pi


def area(radio):
    """float -> float
    OBJ: Área dada el radio
    PRE: radio >= 0"""
    return (radio**2)*pi

print(perimetro(0.5))   # 2 * (1/2) * π = π
print(area(1))          # 1^2 * π = π
