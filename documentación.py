class Areas:

    """ Esta clase calcula las áreas de diferentes figuras geometricas"""

    def areaCuadrado(lado):

        """Calcula el área de un cuadrado elevando al cuadrado el lado
        pasado por parametro"""

        return "El area del cuadrado es: " + str(lado*lado)

    def areaTriangulo(base, altura):

        return "El área del triangulo es: " + str((base*altura)/2)

    # print(areaCuadrado(5))
    # print(areaCuadrado.__doc__)

help(Areas)