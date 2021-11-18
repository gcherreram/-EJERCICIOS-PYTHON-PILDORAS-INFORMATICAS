# def area_triangulo(base, altura):

#     return (base*altura)/2


# triangulo1=area_triangulo(5,7)

# triangulo2=area_triangulo(9,6)


# print(triangulo1)
# print(triangulo2)

# area_triangulo=lambda base, altura:(base*altura)/2

# # no se puede crear funciones lambdas si la función original tiene bucles

# print(area_triangulo(5,7))
# print(area_triangulo(9,6))

# al_cubo=lambda numero:(numero, 3)

# al_cubo=lambda numero:numero**3

# print(al_cubo(13))

destacar_valor=lambda comision:"!{}¡ €".format(comision)

comision_Ana=15585

print(destacar_valor(comision_Ana))