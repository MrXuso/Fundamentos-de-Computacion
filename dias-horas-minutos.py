"""************  SEGUNDOS A DÍAS, HORAS, MINUTOS Y SEGUNDOS  *************
---             Francisco Jesús Jiménez Hidalgo, M48-OCT-2016           """


def aDiasHorasMinsSegs(tiempo):
    """int -> str
    OBJ: Días, horas, minutos y segundos en un tiempo en segundos dado
    PRE: tiempo >= 0"""

    # Calculamos los días
    dias = tiempo // (60 * 60 * 24)

    # Calculamos las horas
    horas = (tiempo // (60 * 60)) % 24

    # Calcuamos los minutos
    minutos = (tiempo // 60) % 60

    # Calculamos los segundos
    segundos = tiempo % 60

    return str(tiempo) + " segundos son " \
           + str(dias) + " días, " \
           + str(horas) + " horas, " \
           + str(minutos) + " minutos y " \
           + str(segundos) + " segundos."

# Pedimos al usuario que introduzca un número de segundos y mostramos el resultado
print("SEGUNDOS A DÍAS, HORAS, MINUTOS Y SEGUNDOS\n"
      + "------------------------------------------ \n\n"
      + "Introduzca un número entero y positivo de segundos: ", end="")

print("\n" + aDiasHorasMinsSegs(int(input())))
