# def areaTriangulo(base, altura):

#     """ 
#     Calcula el área de un triangulo dado

#     # Lo que se espera entra aquí
#     >>> areaTriangulo(3,6)
#     'El área del triangulo es: 9.0'

#     """

#     return "El área del triangulo es: " + str((base*altura)/2)

# Módulo para realizar pruebas, 

def compruebaMail(mailUsuario):

    """
    La función compruebaMail evalúa un mail recibido en busca de la @. Si
    tiene una @ es correcto, si tiene mas de una @ es incorrecto, si la
    @ esta al final es incorrecto

    >>> compruebaMail('juan@cursos.es')
    True

    >>> compruebaMail('juancursos.es@')
    False

    >>> compruebaMail('juancursos.es')
    False

    >>> compruebaMail('juan@cursos@.es')
    False

    """

    arroba=mailUsuario.count('@')

    if (arroba!=0 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
        return False
    else:
        return True

import doctest
doctest.testmod()